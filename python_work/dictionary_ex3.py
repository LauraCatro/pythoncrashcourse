# Ex 1
favorites_places = {
    'Diana': 'Casa',
    'Carlos': 'Escuela',
    'Angeles': 'Playa',
}

for person, place in favorites_places.items():
    print(f"El lugar favorito de {person.title()} es la {place.lower()}")

# Ex2
favorite_numbers = {
    'diana': [5, 2],
    'angeles': [11, 12],
    'victor': [8, 10],
    'daniel': [34, 67],
    'rodrigo': [21, 34],
}

for person, numbers in favorite_numbers.items():
    print(f"The favorites numbers of {person.title()} are: ")
    for number in numbers:
        print(f"\t{number}")
