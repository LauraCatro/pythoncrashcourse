pizzas = ['Pepperoni', 'Hawaiana', 'Mexicana']
for pizza in pizzas:
    print(f"I like {pizza.lower()} pizza.\n")
print("I really love pizza")

friend_pizzas = pizzas[:]

pizzas.append('Frijoles')
friend_pizzas.append('Queso')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
