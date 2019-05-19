import mysql.connector

username = input("enter user:\n")
password = input("enter password:\n")
#conect to db
conn = mysql.connector.connect(
	host = "localhost",
	user = username,
	passwd = password
)

print(conn)


cursor = conn.cursor()

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


create_db = open("create_database.sql")
create_db = create_db.read()
cursor.execute(create_db)

conn.close()