def city_and_county(city, country, population=''):
    if population:
        full_name_population = f"{city}, {country}- Population {population}"
    else:
        full_name_population = f"{city}, {country}"
    return full_name_population.title()

