def make_sandwiches(*toppings):
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")


make_sandwiches('onion')
make_sandwiches('cheese', 'tomato', 'lettuce')
