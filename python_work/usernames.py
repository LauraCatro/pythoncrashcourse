current_users = ['estrella','angela','berry','lucas','dany']
new_users = ['Estrella','Fredy','Lucas','Dany','Diana']

for user in new_users:
    if user.lower() in current_users:
        print("Este nombre no esta disponible")
    else:
        print(f"Este nombre esta disponible {user}")