import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)


dbCursor = db_connection.cursor()
dbCursor.execute("UPDATE Students SET name='Jame' WHERE id = 102")
db_connection.commit()
dbCursor.execute("SELECT id,name,age FROM Students")
for db in dbCursor:
    print("%d %s %d"%(db[0],db[1],db[2]))