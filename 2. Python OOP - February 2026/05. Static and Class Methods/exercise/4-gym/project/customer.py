class Customer:
    CUSTOMER_ID = 1
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        id = Customer.CUSTOMER_ID
        Customer.CUSTOMER_ID += 1
        return id
    
    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"