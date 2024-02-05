class Products:
    def __init__(self, product_id, product_name, description, price):
        self.ProductID = product_id
        self.ProductName = product_name
        self.Description = description
        self.Price = price

    def get_product_details(self):
        print(f'ProductID: {self.ProductID}, ProductName: {self.ProductName}, Description: {self.Description}, Price: {self.Price}')

    def update_product_info(self, price=None, description=None):
        if price is not None:
            self.Price = price
        if description is not None:
            self.Description = description

    def is_product_in_stock(self):
        # Add implementation logic to check if the product is in stock
        return True
