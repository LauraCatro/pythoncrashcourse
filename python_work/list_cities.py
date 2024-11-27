cities = ['CDMX', 'Bogota', 'Hidalgo', 'New York',
          'Milan', 'Monaco', 'Seul', 'Madrid', 'Roma']
message = f"I love {cities[0]}"
# Original cities
print(cities)
# Acces a element
print(cities[5])
# Format a element
print(cities[4].upper())
# The last element
print(cities[-1])
# Print message
print(message)
# Modify
cities[1] = 'Toronto'
print(f"New list: {cities}")
# Appending element
cities.append('Los Angeles')
print(cities)
# Insert elements
cities.insert(0, 'Orlando')
print(cities)
# remove using del
del cities[0]
print(cities)
# remove using pop
propped_city = cities.pop()
print(cities)
print(propped_city)
# Remove using value
cities.remove('Hidalgo')
print(cities)
# Sort list alphabetical
print("This list is sort alphabetical")
print(sorted(cities))
# Sorted list reverse-alphabetical
print("This list is sort reverse-alphabetical")
print(sorted(cities, reverse=True))
# Sort list
cities.sort
print(cities)
# list reverse
cities.reverse()
print(cities)
