# Ex1
person_0 = {'firts_name': 'Diana',
            'last_name': 'Castro',
            'age': 20,
            'city': 'EDOMEX',
            }

person_1 = {'firts_name': 'Laura',
            'last_name': 'López',
            'age': 21,
            'city': 'CDMX',
            }
person_2 = {'firts_name': 'Daniel',
            'last_name': 'Sol',
            'age': 19,
            'city': 'Monterrey',
            }

persons = [person_0, person_1, person_2]

for person in persons[:]:
    print(f"Firts Name: {person['firts_name']}")
    print(f"Last Name:{person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

# Ex2
favorite_numbers = {
    'diana': 2,
    'angeles': 6,
    'victor': 23,
    'daniel': 56,
    'rodrigo': 7,
}

for person in favorite_numbers:
    print(f"The favorite number of {person.title()} is {
          favorite_numbers[person]}")

# Ex3
glossary = {
    'list': 'List are defined using square brackets []',
    'Dictionary': 'Dictionaries are defined using curly braces {}',
    'Tuple': 'Tuples are defined using parentheses ()',
}

print("Glossay: ")
for word in glossary:
    print(f"{word.title()}")
    print(f"\t{glossary[word]}")


user_0 = {
    'user_name': 'efermi',
    'firts': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"Value: {value}")
