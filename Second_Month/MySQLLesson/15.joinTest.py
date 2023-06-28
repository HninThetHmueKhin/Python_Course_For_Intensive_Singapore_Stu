import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dbCursor = db_connection.cursor()
dbCursor.execute("SELECT Students.id,Students.name,Students.age,cost.id,cost.totalCost,cost.monthly FROM cost join Students on cost.id = Students.id")
data = dbCursor.fetchall()

print("id         name           age   CostID    TotalCost   Monthly")
for db in data:
    print("%d      %s             %d     %d        %d           %d"%(db[0],db[1],db[2],db[3],db[4],db[5]))