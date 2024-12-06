"""A class that can be used to represent a car"""
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# Modifying an Attribute's Value Directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method

# my_new_car.update_odometer(25)
# my_new_car.read_odometer()

# my_new_car.update_odometer(12)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2019)
# print(f"\n{my_used_car.get_descriptive_name()}")

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()