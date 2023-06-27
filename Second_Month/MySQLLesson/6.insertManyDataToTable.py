import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dataType = "INSERT INTO Students(id,name,age,attend,hobby) values(%s ,%s ,%s ,%s ,%s )"
data = [(103,"ST",1000,4,"Travelling"),(104,"WT",1010,4,"Reading")]

dbCursor = db_connection.cursor()
dbCursor.executemany(dataType,data)

db_connection.commit()
print("Datas are inserted!")
print(dbCursor.rowcount)

dbCursor.execute("SELECT * FROM Students")
for tb in dbCursor:
    print(tb)