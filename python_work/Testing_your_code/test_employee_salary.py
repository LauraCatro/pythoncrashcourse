import pytest
from employee_class import Employee


@pytest.fixture
def employee_salary():
    salary = None
    employee_salary = Employee('Diana', 'Castro', salary)
    return employee_salary


def test_give_default_raise(employee_salary):
    employee_salary.give_raise()
    assert employee_salary.annual_salary == 5000


def test_give_custom_raise(employee_salary):
    employee_salary.give_raise(1000)
    assert employee_salary.annual_salary == 1000
