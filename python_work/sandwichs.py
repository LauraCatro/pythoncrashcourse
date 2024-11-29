sandwich_orders = ['Ham', 'Beans', 'Egg', 'pastrami', 'pastrami', 'pastrami']
finished_sandwich = []

print("We no longer have pastrami sandwiches")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for sandwich in sandwich_orders:
    print(f"I made your {sandwich.lower()} sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)

for sandwich in finished_sandwich:
    print(f"This {sandwich} sandwich is made")
