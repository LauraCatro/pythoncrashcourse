from User_class import User

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
