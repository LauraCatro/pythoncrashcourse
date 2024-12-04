class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe name of the restaurant is: {self.restaurant_name} ")
        print(f"The type of cuisine is: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is open!")


restaurant = Restaurant('The Green Fork','Vegetarian Cuisine')
restaurant_1 = Restaurant('Spice Haven', 'Indian Cuisine')
restaurant_2 = Restaurant('Bella Pasta','Italian Cuisine')

restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
        