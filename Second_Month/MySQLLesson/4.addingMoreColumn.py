import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dbCursor = db_connection.cursor()
dbCursor.execute("alter table Students ADD hobby VARCHAR (20)")
dbCursor.execute("DESCRIBE Students")
for tb in dbCursor:
    print(tb)