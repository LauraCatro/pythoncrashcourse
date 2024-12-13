from city_functions import city_and_county

def test_city_and_county_population():
    city_country_population = city_and_county('Santiago','Chile','6543')
    assert city_country_population == 'Santiago, Chile- Population 6543'
