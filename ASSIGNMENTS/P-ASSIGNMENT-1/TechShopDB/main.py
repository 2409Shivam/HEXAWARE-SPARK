from datetime import datetime
from Customers import Customers
from Products import Products
from Orders import Orders
from OrderDetails import OrderDetails
from Inventory import Inventory

def main():
    # Create sample instances
    shivam = Customers(customer_id=1, first_name="Shivam", last_name="Singh", email="shivasingh414@gmail.com",
                       phone="8340508631", address="Street 12 Sector 9/B Bokaro Steel City Jharkhand ")

    # Create sample instances
    laptop = Products(product_id=1, product_name="Iphone 15 pro max", description="Real Titanium 1TB", price=150000)

    # Create sample instances
    order = Orders(order_id=1, customer=shivam, order_date=datetime.now(), total_amount=150000)

    # Create sample instances
    order_detail = OrderDetails(order_detail_id=1, order=order, product=laptop, quantity=2)

    # Create sample instances
    laptop_inventory = Inventory(inventory_id=1, product=laptop, quantity_in_stock=10, last_stock_update=datetime.now())

    # Interactive menu for testing
    while True:
        print("\nTechShop Management System")
        print("1. View Customer Details")
        print("2. View Product Details")
        print("3. View Order Details")
        print("4. View Inventory Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            shivam.get_customer_details()

        elif choice == "2":
            laptop.get_product_details()

        elif choice == "3":
            order.get_order_details()

        elif choice == "4":
            laptop_inventory.list_all_products()

        elif choice == "5":
            print("Exiting TechShop Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
