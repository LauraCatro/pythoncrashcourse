from random import choices

characters = ['A', 'V', 'G', 'E', 'T', 'Y',
              'P', 'W', 'Z', 'E', 23, 45, 12, 2, 56]
choosen_characters = choices(characters, k=4)

my_ticket = choices(characters, k=4)

winner_ticket = []
count = 0
while winner_ticket != my_ticket:
    winner_ticket = choices(characters, k=4)
    count += 1
print(f"My ticket {my_ticket}")
print(f"Winner ticket{winner_ticket}")
print(f"¿How many times the loop had to run to give you a winning ticket? {count}")