sandwich_orders = ['jamon', 'frijoles', 'huevo']
finished_sandwich = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich.lower()} sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    finished_sandwich.append(sandwich)

for sandwich in finished_sandwich:
    print(f"This sandwich de {sandwich} esta hecho")