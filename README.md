# ccf-db-migration

Migrating solid database to mysql database using python and creating frontend to query database


##To Use

1. Install MySql

2. Create DB with username and password

3. run main.py, changing relevant paths to where the data files are
	takes about 1 min for patient, 1.5 min for study, 0 min for media, 0.5 min for media_detail, 10 min for video_record

4. Install WAMP

5. Stop IIS from running, so localhost refers to WAMP www folder. To do so, run command prompt as admin, and type "iisreset /stop"

6. Right click on wamp, click start all services, should automatically connect to mysql db. Can check by right clicking wamp, logging into mysql server, and checking that "mydatabase" is located on left.

7. Change username and password in home.php to whatever database credentials are.

8. https://mysqlserverteam.com/upgrading-to-mysql-8-0-default-authentication-plugin-considerations/
The location of mysql config file was C:\ProgramData\MySQL\MySQL Server 8.0\
so steps are to edit the mysql file, use "net stop MySQL80" in command prompt, click on mysql.exe in C:\Program Files\MySQL\MySQL Server 8.0\bin, and then restart all services in wampserver (make sure icon is green not red/orange)


9. Move home.php into C:\wamp64\www, can now go to localhost/home.php to see it. Media Name query not yet implemented.

