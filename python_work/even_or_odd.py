number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is even")
else: 
    print(f"\nThe number {number} is odd")

