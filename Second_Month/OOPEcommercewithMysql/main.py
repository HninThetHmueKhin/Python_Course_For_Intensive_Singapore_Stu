import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database = "ecommerce_db_online"
)
cursor = db.cursor()

#Product Class
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = None

    def save_to_database(self):
        query = "INSERT INTO products(name,price,quantity) VALUES(%s, %s, %s)"
        values = (self.name,self.price,self.quantity)
        cursor.execute(query,values)
        db.commit()
        self.id = cursor.lastrowid

    @staticmethod
    def get_all_products():
        query = "SELECT * FROM products"
        cursor.execute(query)
        return cursor.fetchall()

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.id = None

    def save_to_database(self):
        query = "INSERT INTO customers(name,email,address) VALUES(%s, %s, %s)"
        values = (self.name, self.email, self.address)
        cursor.execute(query, values)
        db.commit()
        self.id = cursor.lastrowid

    @staticmethod
    def get_all_customer():
        query = "SELECT * FROM customers"
        cursor.execute(query)
        return cursor.fetchall()

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def save_to_database(self):
        self.customer.save_to_database()

        query = "INSERT INTO orders (customer_id) VALUES (%s)"
        values = (self.customer.id,)
        cursor.execute(query,values)
        db.commit()

        #order id
        order_id = cursor.lastrowid

        for product in self.products:
            product.save_to_database()
            query = "INSERT INTO ordered_products (order_id,product_id) VALUES (%s , %s)"
            values = (order_id,product.id)
            cursor.execute(query, values)
            db.commit()

    @staticmethod
    def get_all_orders():
        query = "SELECT * FROM orders"
        cursor.execute(query)
        return cursor.fetchall()

if __name__ == '__main__':
    product1 = Product("P001",10.99,5)
    product2 = Product("P002", 100.99, 3)
    product3 = Product("P003", 100.99, 15)

    customer = Customer("John","john@gmail.com","123 Main Street A")

    order = Order(customer,[product1,product2,product3])
    order.save_to_database()

    #Retrieve all products from db
    products = Product.get_all_products()
    for product in products:
        print(product)

    # Retrieve all customers from db
    customers = Customer.get_all_customer()
    for customer in customers:
        print(customer)

    # Retrieve all customers from db
    orders = Order.get_all_orders()
    for order in orders:
        print(order)

db.close()
