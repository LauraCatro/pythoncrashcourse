prompt = "\nPlease enter the toppings for your pizza"
prompt += "\n(Enter 'quit' when you are finished) "

# Primera forma
while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"You add {topping.lower()} on your pizza")

# Segunda forma

# topping = ""

# while topping != 'quit':
#    topping = input(prompt)

#    if topping != 'quit':
#        print(f"You add {topping} on your pizza")

# Tercer forma

# active = True

# while active:
#    topping = input(prompt)

#   if topping == 'quit':
#        active = False
#    else:
#        print(f"You add {topping} on your pizza")
