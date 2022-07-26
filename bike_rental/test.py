import unittest
from datetime import datetime, timedelta
from bike_rental import BikeRental, Customer


class BikeRentalTest(unittest.TestCase):

    def test_Bike_Rental_displays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)

    def test_rentBikeonHourlyBasis_for_negative_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonHourlybasis(-1), None)

    def test_rentBikeonHourlyBasis_for_zero_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonHourlybasis(0), None)

    def test_rentBikeonHourlyBasis_for_valid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeonHourlybasis(2).hour, hour)

    def test_rentBikeonHourlyBasis_for_invalid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonHourlybasis(11), None)

    def test_rentBikeonDailyBasis_for_negative_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonHourlybasis(-1), None)

    def test_rentBikeonDailyBasis_for_zero_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonDailyBasis(0), None)

    def test_rentBikeonDailyBasis_for_valid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeonDailyBasis(2).hour, hour)

    def test_rentBikeonDailyBasis_for_invalid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonDailyBasis(11), None)

    def test_rentBikeonweeklyBasis_for_zero_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonWeeklyBasis(0), None)

    def test_rentBikeonweeklyBasis_for_zero_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonWeeklyBasis(0), None)

    def test_rentBikeonweeklyBasis_for_valid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeonWeeklyBasis(2).hour, hour)

    def test_rentBikeonweeklyBasis_for_invalid__positive_numbers_of_bike(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeonWeeklyBasis(11), None)

    def test_returnBike_for_invalid_rentalTime(self):
        # create shop and customer

        shop = BikeRental(10)
        customer = Customer()

        # let the customer who did not rent a bike try to return one

        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))

        # manually check return function with error values
        self.assertIsNone(shop.returnBike((0, 0, 0)))

    def test_returnBike_for_invalid_rentalBasis(self):
        # create shop and customer

        shop = BikeRental(10)
        customer = Customer()

        # create a valid rentaltime and Bike
        customer.rentalTime = datetime.now()
        customer.bikes = 3

        # create an invalid rental basis
        customer.rentalBasis = 7

        request = customer.returnBike()
        self.assertEqual(shop.returnBike(request), 0)

    def test_returnBike_for_Invalid_numofBikes(self):
        shop = BikeRental(10)
        customer = Customer()
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1

        # create invalid bikes

        customer.bikes = 0

        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))

    def test_returnBike_for_valid_credentials(self):
        # create shop and various customers

        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()

        # create a valid rentalBasis for each customer
        customer1.rentalBasis = 1
        customer2.rentalBasis = 1
        customer3.rentalBasis = 2
        customer4.rentalBasis = 4
        customer5.rentalBasis = 6

        # create valid bikes for each customer
        customer1.bikes = 1
        customer2.bikes = 2
        customer3.bikes = 5
        customer4.bikes = 9
        customer5.bikes = 11

        # create past valod rental times for each customer

        customer1.rentalTime = datetime.now() + timedelta(hours=4)
        customer2.rentalTime = datetime.now() + timedelta(hours=23)
        customer3.rentalTime = datetime.now() + timedelta(hours=2)
        customer4.rentalTime = datetime.now() + timedelta(hours=23)
        customer5.rentalTime = datetime.now() + timedelta(hours=8)

        # make all customers return bikes
        request1 = customer1.returnBike()
        request2 = customer2.returnBike()
        request3 = customer3.returnBike()
        request4 = customer4.returnBike()
        request5 = customer5.returnBike()

        # check if all of them got the correct bill
        self.assertEqual(shop.returnBike(request1), 20)
        self.assertEqual(shop.returnBike(request2), 50)
        self.assertEqual(shop.returnBike(request3), 100)
        self.assertEqual(shop.returnBike(request4), 22)
        self.assertEqual(shop.returnBike(request5), 99)


class CustomerTest(unittest.TestCase):
    def test_return_Bike_with_valid_input(self):
        # create customer
        customer = Customer()

        # create a valid rentalTime, rentalBasis, bikes
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.bikes = 1

        self.assertEqual(customer.returnBike(), (now, 1, 1))

    def test_return_Bike_with_invalid_input(self):
        # create customer
        customer = Customer()

        # create a valid rentalTime, rentalBasis, bikes
        customer.rentalBasis = 1
        customer.bikes = 0

        # create invalid rental time
        customer.rentalTime = 0
        self.assertEqual(customer.returnBike(), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
