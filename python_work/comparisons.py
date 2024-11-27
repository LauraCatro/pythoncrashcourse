requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again")


# cheking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'maria'

if user not in banned_users:
    print(f"{user.title()}, you can post")
