from customer import Customer

class Customers:
    def __init__(self):
        self.customers = []

    def addCustomer(self, c):
        self.customers.append(c)

    def removeCustomer(self, c):
        self.customers.remove(c)