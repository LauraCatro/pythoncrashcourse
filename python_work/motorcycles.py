motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Appending elements to the end of a list
motorcycles.append('ducati')
print(motorcycles)

# Insert elements in a list
motorcycles.insert(0, 'Italika')
print(motorcycles)

# Remove an item using 'del'
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Remove using a value
motorcycles.remove('ducati')
print(motorcycles)

# Renive using a variable
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

# Change element of a list
# motorcycles[0] = 'ducati'
# print(motorcycles)

# Add elements in a empty list
cars = []

cars.append('Toyota')
cars.append('Honda')
cars.append('Nissan')

print(cars)

# Removing using pop()
popped_cars = cars.pop()
print(cars)
print(popped_cars)

last_owned = cars.pop()
print(last_owned)
print(f"The last car i owned was a {last_owned}")
