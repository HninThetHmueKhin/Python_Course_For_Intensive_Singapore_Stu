import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dataType = "INSERT INTO Students(id,name,age,attend,hobby) values(%s ,%s ,%s ,%s ,%s )"
data = (102,"NT",101,4,"Research")

dbCursor = db_connection.cursor()
dbCursor.execute(dataType,data)

db_connection.commit()
print("Data are inserted!")
print(dbCursor.rowcount)

dbCursor.execute("SELECT * FROM Students")
for tb in dbCursor:
    print(tb)