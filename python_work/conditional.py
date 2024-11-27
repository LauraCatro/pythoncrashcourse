car = 'Honda'

print("The car is a Honda? ")
print(car.lower() == 'honda')

print("\nThe car is a Audi?")
print(car.lower() == 'audi')

object = 'Phone'

print("The object is a phone?")
print(object.lower() == 'phone')

print("\nThe object is a TV?")
print(object.lower() == 'tv')

city = 'CDMX'

print("The city is CDMX?")
print(city.lower() == "cdmx")

print("\nThe city is Toronto?")
print(city.lower() == "toronto")

# Test equality and inequality

print(car == 'Honda')
print(car != 'Audi')

# Numerical test

number_1 = 10
number_2 = 30

print(number_1 < 35)
print(number_1 > 11)
print(number_2 <= 30)
print(number_2 >= 50)

# Using AND/OR

print(number_1 < 35 and number_2 < 50)
print(number_1 > 9 or number_2 > 25)

# is o not in the list?

users = ['Carlos', 'Viviana', 'Diana']

user = 'David'

if user in users:
    print("Is in the list")

else:
    print("Is not in the list")
