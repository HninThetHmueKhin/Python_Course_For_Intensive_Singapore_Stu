import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
)

#creating a cursor object
db_cursor = db_connection.cursor()
# db_cursor.execute("CREATE DATABASE onlineDB1")
db_cursor.execute("SHOW DATABASES")
for db in db_cursor:
    print(db)