guests = ['Victor', 'Diana', 'Angeles']

print(f"Hello {guests[0].title()}, I would like to invite you to get a dinner")
print(f"Hello {guests[1].title()}, I would like to invite you to get a dinner")
print(f"Hello {guests[2].title()}, I would like to invite you to get a dinner")

print(guests[2])

guests[2] = 'Viviana'
print(guests)

print(f"Hello {guests[0].title()}, I would like to invite you to get a dinner")
print(f"Hello {guests[1].title()}, I would like to invite you to get a dinner")
print(f"Hello {guests[2].title()}, I would like to invite you to get a dinner")

guests.insert(0, 'Angelica')
guests.insert(0, 'Valeria')
guests.append('Jaziel')

print(guests)

guest_remove = guests.pop()
print(guest_remove)
print(f"I'm sorry {guest_remove} i can't invite you")

guest_remove = guests.pop()
print(guest_remove)
print(f"I'm sorry {guest_remove} i can't invite you")

del guests[-1]
del guests[-2]
print(guests)

del guests[1]
del guests[0]
print(guests)

