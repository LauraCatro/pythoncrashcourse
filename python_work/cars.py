cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# Reverse alphabetical
cars.sort(reverse=True)
print(cars)

# Sorting a list Temporarily
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the soriginal list again: ")
print(cars)

# Printing a list in reverse order
cars.reverse()
print(cars)

#If statement
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
