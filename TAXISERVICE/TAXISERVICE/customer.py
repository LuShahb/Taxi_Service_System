
class Customer:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.need_taxi = False

    def request_taxi(self):
        self.need_taxi = True



