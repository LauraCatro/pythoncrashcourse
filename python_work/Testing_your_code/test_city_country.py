from city_functions import city_and_county

def test_city_country():
    full_name = city_and_county('Santiago', 'Chile')
    assert full_name == 'Santiago, Chile'

