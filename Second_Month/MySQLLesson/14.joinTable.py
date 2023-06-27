import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dbCursor = db_connection.cursor()
dbCursor.execute("CREATE TABLE cost(id int primary key AUTO_INCREMENT,monthly int,totalCost int)")

dataType = "INSERT INTO cost(id,monthly,totalCost) values(%s ,%s ,%s)"
data = [(103,150,1500),(104,100,1200),(105,250,2500)]

dbCursor.executemany(dataType,data)

db_connection.commit()
print("Datas are inserted!")

dbCursor.execute("SELECT Students.id,Students.name,Students.age,cost.id,cost.totalCost,cost.monthly FROM cost join Students on cost.id = Students.id")
data = dbCursor.fetchall()
print(data)
# print("id         name           age   CostID    TotalCost   Monthly")
for db in dbCursor:
    print("%d %s %d %d %d %d"%(db[0],db[1],db[2],db[3],db[4],db[5]))