dimensions = (200, 50)
# Error
# dimension[0] = 250
print(dimensions)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("Original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimension")
for dimension in dimensions:
    print(dimension)
