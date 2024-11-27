available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni'
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'freanch fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don´t have {requested_topping}")
print("\nFinished making your pizza")

# for request_topping in requested_toppings:
#   if request_topping == 'green peppers':
#        print("Sorry, we are out of green peppers rigth now")
#    else:
#        print(f"Adding {request_topping}.")

# if 'mushrooms' in requested_toppings:
#   print("Adding mushrooms")
# if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni")
# if 'extra cheese' in requested_toppings:
#   print("Adding extra cheese")
# print("\nFinished making your pizza")


# fruits = ['Banana','Orange','Apple','WaterMelon','Blueberry']
# fruit = 'BlueBerry'

# if 'Banana' in fruits:
#   print("You really like Banana")
# if 'WaterMelon' in fruits:
#    print("You really like WaterMelon")
# if 'Orange' in fruits:
#    print("You really like Orange")
# if 'Apple' in fruits:
#    print("You really like Apple")
# if 'Blueberry' in fruits:
#    print("You really like Blueberry")
