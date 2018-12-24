from driver import Driver
from drivers import Drivers
from customer import Customer
from taxi_service import Taxi
from dispatcher import Dispatcher
from customers import Customers


def main():
    taxi1 = Taxi('Kia')

    dr1 = Driver('Armen', 1)
    dr2 = Driver('Karen', 2, 'Free')
    dr3 = Driver('Aram', 3, 'Busy')

    dr_list = Drivers()
    dr_list.addDriver(dr1)
    dr_list.addDriver(dr2)
    dr_list.addDriver(dr3)

    cus1 = Customer('Mari', 1)
    cus2 = Customer('Ani', 2)
    cus_list = Customers()
    cus_list.addCustomer(cus1)
    cus_list.addCustomer(cus2)
    print(cus_list.customers)
    dis = Dispatcher(dr_list)

    taxi1.drivers = dr_list
    taxi1.customers = cus_list.customers
    taxi1.dispatcher = dis
    print(taxi1.customers)
    cus1.request_taxi()
    ride1 = taxi1.start_ride()
    print(ride1.created_at)

if __name__ == '__main__':
    main()

