# A Bike Rental System

This a full fledged bike rental system created using object oriented programming.

## Customers can:
- See available bikes on the shop.
- Rent bikes on hourly basis
- Rent bikes on a daily basis
- Rent bike on a weekly basis
- There is also a family rental promotion that can range from 3 to 5 Rentals with discount of 30% of the total price

## The bike rental shop can:
- Issue a bill when customers decide to return the bike
- display available inventory
- Take requests on hourly, daily and weekly basis by cross verifying stock

To make it easy, we assume that:
1. Any customer requests rentals of only one type
2. Free to chose the number of bikes he/she wants
3. Requested bikes should be less than available stock.

Code is displayed below

```
"""import modules"""

import datetime


class BikeRental:
    def __init__(self, stock=0):
        """
        The constructor class used to instantiate bike rental shop
        """
        self.stock = stock

    def displaystock(self):
        """
        Displays if the bike is currently available for rent in the shop
        """

        print(f"We currently have {self.stock} available in the shop for rent")
        return self.stock

    def rentBikeonHourlybasis(self, n):
        """
        rents bike on hourly basis to users
        """
        # way to reject invalid input

        if n <= 0:
            print("The number of bikes entered should be greater than 0")
            return None

        # do not rent bike if stock is less than the number of requested bikes

        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available for rent ")
            return None

        # rent the bike

        else:
            now = datetime.datetime.now()
            print(f"You have rented a {n, now.hour} on a hourly basis")
            print(f"You will be charged $3 for each hour per bike")
            print("Have a wonderful ride!")

            self.stock -= n
            return now

    def rentBikeonDailyBasis(self, n):
        """
        Rents bike to users on a daily basis
        """

        if n <= 0:
            print("The number of bikes entered should be greater than 0")
            return None

        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available for rent ")
            return None

        else:
            now = datetime.datetime.now()
            print(f"You have rented a {n, now.hour} on a daily basis")
            print(f"You will be charged $20 for each daily per bike")
            print("Have a wonderful ride!")

            self.stock -= n
            return now

    def rentBikeonWeeklyBasis(self, n):
        """
        Rents bike to users on a weekly basis
        """

        if n <= 0:
            print("The number of bikes entered should be greater than 0")
            return None

        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available for rent ")
            return None

        else:
            now = datetime.datetime.now()
            print(f"You have rented a {n, now.hour} on a weekly basis")
            print(f"You will be charged $140 for each week per bike")
            print("Have a wonderful ride!")

            self.stock -= n
            return now

    def returnBike(self, request):
        """
        1. will accept a rented bike from a user
        2. Repleishes the inventory
        3. Return a bill
        """

        # extracts the initial bill

        rentalTime, rentalBasis, numofBikes = request
        bill = 0

        # will issue a bill if the above parameters are not null

        if rentalTime and rentalBasis and numofBikes:
            self.stock += numofBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numofBikes

            # daily bill calculation

            if rentalBasis == 1:
                bill = round(rentalPeriod.days / 7) * 60 * numofBikes

                # family discount calculation

            if (3 <= numofBikes <= 5):
                print("You are eligible for our family discount promotion")
                return bill

            else:
                print("Are you sure you rented a bike with us")
                return None


class Customer:
    def __init__(self):
        """
        constructor to instantiate various customer objects
        """

        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        """
        Will take a request from the customers for the number of bikes
        """

        bikes = input("How many bikes do you want")

        # In case of invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That is not a positive number")
            return -1

        if bikes < 1:
            print("Invalid input! Number of bikes should be greater than 0")
            return -1
        else:
            self.bikes = bikes

    def returnBike(self):
        """
        Allows customers to return their bikes
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0

```

## Test Driven Development(TDD)
- Test saves time
- Identifies and prevents problems
- Makes your code more attractive
- Helps for better team work

To test the code, I will use Unit test, which is one of the many ways codes can be tested

 ## Note the following:
- Test methods follow snakecase
- Test methods are descriptive
- Always test for very extreme inputs like null values, zero arrays, non-integers, inputs, invalid dates
- test files will often run longer than the main program

## Code for unit test

```
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

```

### Running the tests

To run the tests, run the command below:
- for python 2.7: py.test test.py
- for python3.4+: pytest test.py

### Common pytest options:
- `v`: enable verbose output
- `-x`: stop running tests on first failure
- `--ff`: run failures from previous test before running other test cases

### How to run:
This code is written using python3. Simply run

```
python3 bike_rental.py
```
