cities = {
    'CDMX': {
        'Country': 'Mexico',
        'Population': 568797007
    },
    'Toronto': {
        'Country': 'Canada',
        'Population': 80000000
    },
    'Los Angeles': {
        'Country': 'United states',
        'Population': 2534262
    },
}

for city, city_info in cities.items():
    print(f"\nCity:{city}")
    country = city_info['Country']
    population = city_info['Population']

    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
