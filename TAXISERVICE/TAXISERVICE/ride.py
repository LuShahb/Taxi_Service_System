import datetime

class Ride:

    def __init__(self, current_customer, current_driver):
        self.customer = current_customer
        self.driver = current_driver
        self.created_at = datetime.datetime.now()
        self.status = 'Waiting'


    def _find_nearest_taxi(order, Drivers):
        for i in range(1, len(Drivers)):
            Driver = Drivers[i]




