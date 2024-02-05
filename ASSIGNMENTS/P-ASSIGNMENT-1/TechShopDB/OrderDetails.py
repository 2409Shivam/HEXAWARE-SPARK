class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.OrderDetailID = order_detail_id
        self.Order = order
        self.Product = product
        self.Quantity = quantity

    def calculate_subtotal(self):
        # Add implementation logic to calculate subtotal for this order detail
        return self.Product.Price * self.Quantity

    def get_order_detail_info(self):
        print(f'OrderDetailID: {self.OrderDetailID}, Product: {self.Product.ProductName}, Quantity: {self.Quantity}, Subtotal: {self.calculate_subtotal()}')

    def update_quantity(self, new_quantity):
        self.Quantity = new_quantity

    def add_discount(self, discount_amount):
        # Add implementation logic to apply a discount to this order detail
        pass
