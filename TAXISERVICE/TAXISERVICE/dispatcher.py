from driver import Driver
from drivers import Drivers
from ride import Ride


class Dispatcher:
    def __init__(self, drivers, dispatcher = 'Admin'):
        self.dispatcher = dispatcher
        self.driverlist = drivers

    def release_driver(Driver):

        driver_id = Driver(id)


        if self.status(Driver(id)) != 'Busy':
            print("Driver is on it's way")
        else:
            pass

    def start_ride(self, customer):
        current_dr = self.driverlist.getfreedriver()

        current_ride = Ride(customer, current_dr)
        return current_ride