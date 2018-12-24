class Taxi:
    def __init__(self, name):
        self.name = name
        self.drivers = []
        self.customers = []
        self.dispatcher = 'Admin'

    def start_ride(self):
        for c in self.customers:
            if c.need_taxi == True:
                return self.dispatcher.start_ride(c)
                break

