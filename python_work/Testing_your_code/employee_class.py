class Employee():

    def __init__(self, first_name, last_name, annual_salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_salary=5000):
        self.annual_salary = annual_salary


# employee_1 = Employee('Diana', 'Castro')
# employee_1.give_raise()
# print(employee_1.annual_salary)
