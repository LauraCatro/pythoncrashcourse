current_users = ['estrella','angela','berry','lucas','dany']
new_users = ['estrella','Fredy','Lucas','dany','Diana']

for user in new_users:
    if user != current_users:
        print(f"The user name is available, hi {user}")
    else:
        print("Enter a new user name")