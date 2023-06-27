import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "onlineDB1"
)

dbCursor = db_connection.cursor()
dbCursor.execute("CREATE TABLE Students(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,attend TINYINT)")
dbCursor.execute("DESCRIBE Students")
for tb in dbCursor:
    print(tb)

"""
id  int primary key auto_increment
name varchar(25)
age  smallint#2bytes
attend tinyint#1 byte
"""
"""
Tinyint 1 byte
Smallint 2 byte
Mediumint 3 byte
int 4 bytes
Bigint 8bytes
"""