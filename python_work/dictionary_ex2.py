# Exercise 1
person_0 = {'firts_name': 'Diana',
            'last_name': 'Castro', 'age': 20,
            'city': 'EDOMEX',
            }

for data, information in person_0.items():
    print(f"{data.title()}: {information}")

# Excercise 2
favorite_numbers = {
    'diana': 2,
    'angeles': 6,
    'victor': 23,
    'daniel': 56,
    'rodrigo': 7,
}

for person, number in favorite_numbers.items():
    print(f"The favorite number of {person.title()} is {number}")

# Excercise 3
glossary = {
    'list': 'List are defined using square brackets []',
    'Dictionary': 'Dictionaries are defined using curly braces {}',
    'Tuple': 'Tuples are defined using parentheses ()',
}

print("Glossay: ")
for word, meaning in glossary.items():
    print(f"{word.title()}")
    print(f"\t{meaning}")

# Excercise 4
rivers = {
    'nile': 'egypt',
    'amazon river': 'brazi',
    'mississippi river': 'United States',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(f"{river.title()}")
for country in rivers.values():
    print(f"{country.title()}")

# Excercise 5

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

names = ['jen', 'diana', 'dany', 'phil']

for name in names:
    if name in favorite_languages.keys():
        print(f"{name.title()} thank you")
    else:
        print(f"{name.title()} please participate in the survey")
