import mysql.connector
import db_operations as dbop
import time
import re
import sys

username = input("enter user:\n")
password = input("enter password:\n")

start = time.time()
'''
def get_line_as_array(line):
	info = re.split("',", line) #data is separated by ',' but sometimes, there is just ', like in arch_study #if null is after entry
	#what if there is ,' ? 
	i = 0
	while i < len(info):
		info[i] = info[i].strip("\n") #remove newline characters
		info[i] = info[i].strip("'")#remove quotation marks
		if (",'" in info[i]): # this is the case not taken care of above if null is before entry
			splitted = re.split(",'", info[i])
			del info[i]
			for j in range(0, len(splitted)):
				info.insert(i, splitted[(j*-1)-1])
		if ("L,N" in info[i]): # if multiple nulls in a row
			splitted = re.split(",", info[i]) 
			del info[i]
			for j in range(0, len(splitted)):
				info.insert(i, splitted[(j*-1)-1])
		if (info[i] == "NULL"):
			info[i] = None
		i += 1

	return info'''

def get_line_as_array(line):
	i = 0
	lowest = 0
	info = [line]
	while i < len(info):
		lowest = info[i].find(",", lowest+1)
		if (lowest == -1):
			info[i] = info[i].strip("\n")
			info[i] = info[i].strip("'")
			if (info[i] == "NULL"):
				info[i] = None
			return info  
		if((info[i][lowest-1] in ["'", "L"]) or (info[i][lowest+1] in ["'", "N"]) ):
			first =	info[i][0:lowest]
			second = info[i][lowest+1:]
			info[i] = second
			info.insert(i, first)
			info[i] = info[i].strip("'")
			if (info[i] == "NULL"):
				info[i] = None
			lowest = 0
			i += 1



config = {
	"host" : "localhost",
	"user" : username,
	"passwd" : password,
	"database" : "mydatabase"
}

#conect to db
conn = mysql.connector.connect(
	host = "localhost",
	user = username,
	passwd = password
)

cursor = conn.cursor(buffered = True)

#creating the db
try:
	cursor.execute("DROP DATABASE mydatabase")
	print("database dropped")
except:
	print("database didn't exist, creating new one")
cursor.execute("CREATE DATABASE mydatabase")
print("database created")
conn.database = "mydatabase"

#creates the tables
print("creating tables")
create_patient = open("create_patient.sql")
create_patient = create_patient.read()
cursor.execute(create_patient)
conn.close()


#apprently mysql connections time out so have to recreate???
conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)
create_study = open("create_study.sql")
create_study = create_study.read()
cursor.execute(create_study)
conn.close()

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)
create_media = open("create_media.sql")
create_media = create_media.read()
cursor.execute(create_media)
conn.close()

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)
create_media_detail = open("create_media_detail.sql")
create_media_detail = create_media_detail.read()
cursor.execute(create_media_detail)
conn.close()

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)
create_video_record = open("create_video_record.sql")
create_video_record = create_video_record.read()
cursor.execute(create_video_record)
conn.close()

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)
create_eeg_record = open("create_eeg_record.sql")
create_eeg_record = create_eeg_record.read()
cursor.execute(create_eeg_record)
conn.close()


print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds to create the tables")
start = time.time()

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered = True)



print("adding data")
#fills the tables with data
patient = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_PATIENT.dat")
for line in patient.readlines():
	entry = get_line_as_array(line)
	try:
		dbop.insert_patient(conn, entry[0], entry[1], entry[2], entry[3])
	except KeyboardInterrupt:
		sys.exit()
	except:
		print("this did not work")
		print(entry)
patient.close()


print("done with patient")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds to fill patient")
start = time.time()

study = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_STUDY.dat")
for line in study.readlines():
	entry = get_line_as_array(line)
	dbop.insert_study(conn, entry[0], entry[1], entry[2], entry[3], entry[4])
study.close()


print("done with study")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds  to fill study")
start = time.time()

media = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_MEDIA.dat")
for line in media.readlines():
	entry = get_line_as_array(line)
	dbop.insert_media(conn, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7])
media.close()

print("done with media")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds  to fill media")
start = time.time()


media_detail = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_MEDIA_DETAIL.dat")
for line in media_detail.readlines():
	entry = get_line_as_array(line)
	dbop.insert_media_detail(conn, entry[0], entry[1], entry[2], entry[3])
media_detail.close()


print("done with media_detail")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds  to fill media_detail")
start = time.time()


video_record = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_VIDEO_RECORD.dat")
for line in video_record.readlines():
	entry = get_line_as_array(line)
	try:
		dbop.insert_video_record(conn, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7])
	except KeyboardInterrupt:
		sys.exit()
	except:
		print("this did not work")
		print(entry)
		#likely because of this
		#ttps://stackoverflow.com/questions/35602939/mysql-1292-incorrect-datetime-value
video_record.close()


print("done with video_record")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds  to fill video_record")
start = time.time()


i = 0
eeg_record = open("E:/Documents/arch/archdb_exp2016/ARCHDB_ARCH_EEG_RECORD.dat")
for line in eeg_record.readlines():
	i+=1
	if (i%50==0):
		print(i);
	entry = get_line_as_array(line)
	dbop.insert_eeg_record(conn, entry[0], entry[1], entry[2],entry[3], entry[4], entry[5], entry[6], entry[7],
		entry[8], entry[9], entry[10], entry[11], entry[12], entry[13])
eeg_record.close()

print("done with eeg_record")
print("it took " + str((time.time()-start)//60) + " minutes and " + str((time.time()-start)%60) + " seconds  to fill eeg_record")
start = time.time()




conn.close()
