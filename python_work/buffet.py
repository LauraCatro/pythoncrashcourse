foods = ('beans', 'chiken', 'soup', 'eggs', 'burrito')


def update_tuple(source_tuple, index, new_value):
    source_list = list(source_tuple)
    source_list[index] = new_value
    return tuple(source_list)


print("Original tupla")
for food in foods:
    print(f"\t{food}")

foods = ('beans', 'chiken', 'soup', 'eggs', 'taco')
# foods = update_tuple(foods, 4, 'taco')
print("\nChange 1 item")
for food in foods:
    print(f"\t{food}")

foods = ('hotcakes', 'coffe', 'soup', 'eggs', 'taco')
# foods = update_tuple(foods, 0, 'hotcakes')
# foods = update_tuple(foods, 1, 'coffe')

print("\nChange 2 items")
for food in foods:
    print(f"\t{food}")
