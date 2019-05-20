import mysql.connector
import db_operations as dbop

username = input("enter user:\n")
password = input("enter password:\n")

def get_line_as_array(line):
	info = line.split(",")
	for i in range(0, len(info)):
		info[i] = info[i].strip("\n") #remove newline characters
		info[i] = info[i].strip("'")#remove quotation makrs
		if (info[i] == "NULL"):
			info[i] = None
	return info

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




#apprently mysql connections time out so have to recreate???
conn = mysql.connector.connect(
	host = "localhost",
	user = username,
	passwd = password,
	database = "mydatabase")
cursor = conn.cursor(buffered = True)
conn.autocommit = True





print("adding data")
#fills the tables with data
patient = open("data/patient.dat")
for line in patient.readlines():
	entry = get_line_as_array(line)
	dbop.insert_patient(conn, entry[0], entry[1], entry[2], entry[3])
patient.close()

study = open("data/study.dat")
for line in study.readlines():
	entry = get_line_as_array(line)
	dbop.insert_study(conn, entry[0], entry[1], entry[2], entry[3], entry[4])
study.close()

print("printing tables in mydatabase")
cursor.execute("SHOW TABLES")
conn.commit()
for x in cursor:
    print(x)



media = open("data/media.dat")
for line in media.readlines():
	entry = get_line_as_array(line)
	dbop.insert_media(conn, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7])
media.close()

media_detail = open("data/media_detail.dat")
for line in media_detail.readlines():
	entry = get_line_as_array(line)
	dbop.insert_media_detail(conn, entry[0], entry[1], entry[2], entry[3])
media_detail.close()


video_record = open("data/video_record.dat")
for line in video_record.readlines():
	entry = get_line_as_array(line)
	print(entry)
	dbop.insert_video_record(conn, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7])
video_record.close()

eeg_record = open("data/eeg_record.dat")
for line in eeg_record.readlines():
	entry = get_line_as_array(line)
	dbop.insert_eeg_record(conn, entry[0], entry[1], entry[2],entry[3], entry[4], entry[5], entry[6], entry[7],
		entry[8], entry[9], entry[10], entry[11], entry[12], entry[13])
eeg_record.close()




conn.close()