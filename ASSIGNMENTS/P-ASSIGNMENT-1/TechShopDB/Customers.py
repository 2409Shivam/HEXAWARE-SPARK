class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.CustomerID = customer_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Phone = phone
        self.Address = address
        self.orders = []

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        print(f'CustomerID: {self.CustomerID}, FirstName: {self.FirstName}, LastName: {self.LastName}, Email: {self.Email}, Phone: {self.Phone}, Address: {self.Address}')

    def update_customer_info(self, email=None, phone=None, address=None):
        if email is not None:
            self.Email = email
        if phone is not None:
            self.Phone = phone
        if address is not None:
            self.Address = address
