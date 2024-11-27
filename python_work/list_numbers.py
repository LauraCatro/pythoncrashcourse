for value in range(1, 21):
    print(value)

numbers = []
for value in range(1, 1_000_001):
    numbers.append(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)

threes = [value for value in range(3, 31, 3)]
print(threes)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
