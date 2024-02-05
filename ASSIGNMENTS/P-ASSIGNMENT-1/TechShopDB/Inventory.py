from datetime import datetime

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.InventoryID = inventory_id
        self.Product = product
        self.QuantityInStock = quantity_in_stock
        self.LastStockUpdate = last_stock_update

    def get_product(self):
        # Add logic to retrieve the product associated with this inventory item
        pass

    def get_quantity_in_stock(self):
        # Add logic to get the current quantity of the product in stock
        pass

    def add_to_inventory(self, quantity):
        # Add logic to add a specified quantity of the product to the inventory
        pass

    def remove_from_inventory(self, quantity):
        # Add logic to remove a specified quantity of the product from the inventory
        pass

    def update_stock_quantity(self, new_quantity):
        # Add logic to update the stock quantity to a new value
        pass

    def is_product_available(self, quantity_to_check):
        # Add logic to check if a specified quantity of the product is available in the inventory
        pass

    def get_inventory_value(self):
        # Add logic to calculate the total value of the products in the inventory
        pass

    def list_low_stock_products(self, threshold):
        # Add logic to list products with quantities below a specified threshold, indicating low stock
        pass

    def list_out_of_stock_products(self):
        # Add logic to list products that are out of stock
        pass

    def list_all_products(self):
        # Add logic to list all products in the inventory, along with their quantities
        pass
