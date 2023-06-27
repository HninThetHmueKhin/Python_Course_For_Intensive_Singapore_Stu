import mysql.connector
db_connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor"
)
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db1")
db_cursor.execute("USE ecommerce_db1")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INT AUTO_INCREMENT PRIMARY_KEY,
        name VARCHAR(255),
        price DECIMAL(10,2),
        quantity INT
    )
""")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INT AUTO_INCREMENT PRIMARY_KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255)
    )
""")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY_KEY,
        customer_id INT,
        FOREIGN_KEY (customer_id) REFERENCES customers(id)
    )
""")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders_products(
        id INT AUTO_INCREMENT PRIMARY_KEY,
        order_id INT,
        product_id INT,
        FOREIGN_KEY (order_id) REFERENCES orders(id),
        FOREIGN_KEY (product_id) REFERENCES products(id)
    )
""")

tables = ['products','customers','orders','ordered_products']
for table in tables:
    db_cursor.execute(f'DESCRIBE {table}')
    print(f'Table: {table}')
    for column in db_cursor:
        print(column)

#close
db_cursor.close()
db_connection.close()


