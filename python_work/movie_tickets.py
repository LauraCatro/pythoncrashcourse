prompt = "\nPor favor ingresa tu edad para indicar el costo del boleto: "
prompt += "Enter -1 for exit"

while True:
    x = input(prompt)
    age = int(x)

    if age > 0 and age < 3:
        print("The ticket is free")
    elif age > 3 and age <= 12:
        print("The ticket is $10")
    elif age > 12:
        print("The ticket is $15")
    elif age < 0:
        break
