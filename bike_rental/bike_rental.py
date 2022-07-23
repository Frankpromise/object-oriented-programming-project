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
