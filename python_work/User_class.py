class User:

    def __init__(self, first_name, last_name, age, nacionality):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 1

    def describe_user(self):
        print("\nUser Information: ")
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Age: {self.age}")
        print(f"Nacionality: {self.nacionality}")

    def greet_user(self):
        print(f"\nHello {self.first} {self.last}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_number_login_attempts(self):
        print(f"Number users: {self.login_attempts}")
