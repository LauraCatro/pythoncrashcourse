# Arbitrary Number of Arguments

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"{topping}")


