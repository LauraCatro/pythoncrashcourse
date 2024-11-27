places = ['Colombia', 'Monterrey', 'Estados Unidos', 'Corea', 'Italia']

print("This is the list original")
print(places)

print("\nThis is the sorted list:")
print(sorted(places))

print("\nThis is the reverse sorted list:")
print(sorted(places, reverse=True))

places.reverse()
print(f"This is the list in reverse order {places}")

places.reverse()
print(f"This is the list in original order {places}")

places.sort()
print(f"List in alphabetical order: {places}")
places.sort(reverse=True)
print(f"List in reversalphabetical order: {places}")
