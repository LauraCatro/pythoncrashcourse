class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is: {self.restaurant_name} ")
        print(f"The type of cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is open!")

    def read_number_served(self):
        print(f"Number Served: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('The Green Fork', 'Vegetarian Cuisine')
restaurant.set_number_served(100)
restaurant.read_number_served()
restaurant.increment_number_served(300)
restaurant.read_number_served()
# restaurant_1 = Restaurant('Spice Haven', 'Indian Cuisine')
# restaurant_2 = Restaurant('Bella Pasta','Italian Cuisine')

restaurant.describe_restaurant()
# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
