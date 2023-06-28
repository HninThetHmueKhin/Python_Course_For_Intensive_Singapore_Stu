import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)


dbCursor = db_connection.cursor()
dbCursor.execute("SELECT id,name,age FROM Students")
allData = dbCursor.fetchall()
for db in allData:
    print(db)