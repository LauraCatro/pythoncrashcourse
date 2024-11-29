# def describe_pet(pet_name, anmial_type = 'dog'):
#    print(f"\nI have a {animal_type}")
#    print(f"My {animal_type}'s name is {pet_name.title()}")


# Multple functions calls
# describe_pet('Woody')
# describe_pet('Maca')

# Keyword arguments

# describe_pet(animal_type='hamster',pet_name='harry')

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# Equivalent Function Calls

# A dog name while
describe_pet('while')
describe_pet(pet_name='while')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
