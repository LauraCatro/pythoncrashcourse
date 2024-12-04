class User:

    def __init__(self, first_name, last_name, age, nacionality):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.nacionality = nacionality
    
    def describe_user(self):
        print("\nUser Information: ")
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Age: {self.age}")
        print(f"Nacionality: {self.nacionality}")
    
    def greet_user(self):
        print(f"\nHello {self.first} {self.last}")


user = User('Diana', 'Laura', 20, 'Mexicana')
user_1 = User('Angeles', 'Marquez', 69, 'Mexicana')
user_2 = User('Antonio', 'Herrera', 24, 'Mexicano')

user.describe_user()
user.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()