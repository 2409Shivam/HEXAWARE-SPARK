# main.py
from datetime import datetime
from Customers import Customers
from Products import Products
from Orders import Orders
from OrderDetails import OrderDetails
from Inventory import Inventory
from DatabaseConnector import DatabaseConnector

# Set your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "765795"
db_name = "TechShopDB"

# Create a DatabaseConnector instance
db_connector = DatabaseConnector(host=db_host, username=db_user, password=db_password, database=db_name)

# Open the database connection
db_connector.open_connection()

def insert_data():
    # Create a sample instance for Karthika Mam
    karthika = Customers(customer_id=2, first_name="Karthika", last_name="Mam", email="karthika@example.com",
                          phone="9876543210", address="123 Main Street")

    # Insert data into the Customers table
    db_connector.execute_query(
        "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s, %s)",
        (karthika.CustomerID, karthika.FirstName, karthika.LastName, karthika.Email, karthika.Phone, karthika.Address)
    )

    # Create a sample instance for MacBook
    macbook = Products(product_id=2, product_name="MacBook", description="Apple MacBook Pro", price=2000)

    # Insert data into the Products table for MacBook
    db_connector.execute_query(
        "INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES (%s, %s, %s, %s)",
        (macbook.ProductID, macbook.ProductName, macbook.Description, macbook.Price)
    )

    # Create a sample instance for iPhone
    iphone = Products(product_id=3, product_name="iPhone", description="Apple iPhone 13 Pro", price=1200)

    # Insert data into the Products table for iPhone
    db_connector.execute_query(
        "INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES (%s, %s, %s, %s)",
        (iphone.ProductID, iphone.ProductName, iphone.Description, iphone.Price)
    )

    # Create a sample instance for an order
    order = Orders(order_id=2, customer=karthika, order_date=datetime.now(), total_amount=3200)

    # Insert data into the Orders table
    db_connector.execute_query(
        "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (%s, %s, %s, %s)",
        (order.OrderID, order.Customer.CustomerID, order.OrderDate, order.TotalAmount)
    )

    # Create a sample instance for Inventory
    inventory = Inventory(inventory_id=2, product=macbook, quantity_in_stock=5, last_stock_update=datetime.now())

    # Insert data into the Inventory table
    db_connector.execute_query(
        "INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES (%s, %s, %s, %s)",
        (inventory.InventoryID, inventory.Product.ProductID, inventory.QuantityInStock, inventory.LastStockUpdate)
    )

    # Create a sample instance for OrderDetails
    order_detail = OrderDetails(order_detail_id=2, order=order, product=iphone, quantity=3)

    # Insert data into the OrderDetails table
    db_connector.execute_query(
        "INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)",
        (order_detail.OrderDetailID, order_detail.Order.OrderID, order_detail.Product.ProductID, order_detail.Quantity)
    )

# Insert data
insert_data()

# Close the database connection when done
db_connector.close_connection()
