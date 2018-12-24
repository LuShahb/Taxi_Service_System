from driver import Driver

class Drivers:
    def __init__(self):
        self.drivers = []

    def addDriver(self, d):
        self.drivers.append(d)

    def removeDriver(self, d):
        self.drivers.remove(d)


    def getfreedriver(self):
        for d in self.drivers:
            if d.status == 'Free':
                return d
            else:
                pass



