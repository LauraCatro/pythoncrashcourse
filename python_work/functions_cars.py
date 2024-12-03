def information_cars(manufacturer,model,**car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model_name'] = model
    return car_information

car_profile = information_cars('Honda', 'Civi',
                               color = 'pink',
                               year = 2024)

print(car_profile)