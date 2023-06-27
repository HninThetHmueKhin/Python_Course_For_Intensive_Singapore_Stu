import mysql.connector

# Establish database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor"
)

# Create a cursor object to execute SQL queries
db_cursor = db_connection.cursor()

# Create the database
db_cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db_online")
db_cursor.execute("USE ecommerce_db_online")

# Create the 'products' table
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10, 2),
        quantity INT
    )
""")

# Create the 'customers' table
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255)
    )
""")

# Create the 'orders' table
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
""")

# Create the 'ordered_products' table
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordered_products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        product_id INT,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
""")

# Print the descriptions of the tables
tables = ['products', 'customers', 'orders', 'ordered_products']
for table in tables:
    db_cursor.execute(f"DESCRIBE {table}")
    print(f"Table: {table}")
    for column in db_cursor:
        print(column)

# Close the database connection
db_cursor.close()
db_connection.close()