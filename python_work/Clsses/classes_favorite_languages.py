favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# Looping through a dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
# This code would have exactly the same output if you wrote
# for name in favorite_languages:

# Print a message to a couple of friends about the languages they chose

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

# Using sorted() function

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

# Using value()

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

# Using set()
print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
