import mysql.connector
import db_operations as dbop

username = input("enter user:\n")
password = input("enter password:\n")
#conect to db
conn = mysql.connector.connect(
	host = "localhost",
	user = username,
	passwd = password
)

print(conn)


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
cursor.execute("SHOW DATABASES")
print("printing cursor")
for x in cursor:
	print(x)   

#creates the tables
create_db = open("create_database.sql")
create_db = create_db.read()
cursor.execute(create_db)
conn.close()



#apprently mysql connections time out so have to recreate???
conn = mysql.connector.connect(
	host = "localhost",
	user = username,
	passwd = password,
	database = "mydatabase")
cursor = conn.cursor(buffered = True)
conn.autocommit = True

print("printing mydatabase")
cursor.execute("SHOW tables")

def get_line_as_array(line):
	info = line.split(",")
	for i in range(0, len(info)):
		info[i] = info[i].strip("'")#remove quotation makrs
		info[i] = info[i].strip("\n") #remove newline characters
		if (info[i] == "NULL"):
			info[i] = None
	return info


print("adding data")
#fills the tables with data
patient = open("data/patient.dat")
for line in patient.readlines():
	entry = get_line_as_array(line)
	print(entry)
	dbop.insert_patient(conn, entry[0], entry[1], entry[2], entry[3])
patient.close()

cursor.execute("SELECT * FROM arch_patient")
for row in cursor:
	print(row)

study = open("data/study.dat")
for line in study.readlines():
	entry = get_line_as_array(line)
	print(entry)
	dbop.insert_study(conn, entry[0], entry[1], entry[2], entry[3], entry[4])
study.close()
cursor.execute("SELECT * FROM arch_study")
for row in cursor:
	print(row)


'''
eeg_record = open()
for line in eeg_record.readlines():
	dbop.insert_eeg_record()
eeg_record.close()

media = open()
for line in media.readlines():
	dbop.insert_media()
media.close()

media_detail = open()
for line in media_detail.readlines():
	dbop.insert_media_detail()
media_detail.close()

video_record = open()
for line in video_record.readlines():
	dbop.insert_video_record()
video_record.close()
'''

conn.close()