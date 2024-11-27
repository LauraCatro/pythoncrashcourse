my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
my_foods.append('tacos')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

print("\n\n\tThe firts three items in the list are:")
print(my_foods[:3])

print("\n\tThe items from the middle of the list are:")
print(my_foods[1:4])

print("\n\tThe last three items in the list are:")
print(my_foods[-3:])
