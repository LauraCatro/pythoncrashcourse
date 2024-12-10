def make_shirt(size, message='I love Python'):
    print(f"The size is {size}")
    print(f"The message is {message}")


# make_shirt('M', 'Hello world')
# make_shirt(size='L',message='Bahamas')

# Make a large shirt

make_shirt('EXG')

# Medium shirt
make_shirt('M')

# With different message

make_shirt('S', 'I love NY')

# Function Cities


def describe_city(city, country):
    print(f"{city} is in {country.title()}")


describe_city('CDMS', 'Mexico')
describe_city('Toronto', 'Canada')
describe_city('LA', 'United States')


def city_country(city, country):
    print(f"{city.title()}, {country.title()}")


city_country('CDMX', 'Mexico')
city_country('Toronto', 'Canada')
city_country('Roma', 'italia')
