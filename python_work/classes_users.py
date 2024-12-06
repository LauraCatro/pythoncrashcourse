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


class Privileges:
    def __init__(self,
                privileges=['can add a post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("The administratator can perform the following actions ")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):

    def __init__(self, first_name, last_name,
                 age, nacionality):
        super().__init__(first_name, last_name, age, nacionality)
        self.privileges = Privileges()


user = User('Diana', 'Laura', 20, 'Mexicana')
# user_1 = User('Angeles', 'Marquez', 69, 'Mexicana')
# user_2 = User('Antonio', 'Herrera', 24, 'Mexicano')

user.describe_user()
print(f"{user.login_attempts}")

# Increment login attempts
user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.read_number_login_attempts()

# Reset Login attempts
user.reset_login_attempts()
user.read_number_login_attempts()

# user_1.describe_user()
# user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

admin = Admin('Carlos', 'Castro', 18, 'Mexicano')
admin.describe_user()
admin.privileges.show_privileges()