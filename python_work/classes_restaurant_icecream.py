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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors=['Strawberry', 'Lemon', 'Chocolate']):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def decribe_flavors(self):
        print("Ice cream flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

# flavors = ['fresa','chocolate','limon']


ice = IceCreamStand('La michoacana', 'Ice cream')
ice.describe_restaurant()
ice.decribe_flavors()
