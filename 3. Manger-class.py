# Class 1
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:",self.name)
        print("Age:", self.age)

# Class 2
class Employee:
    def _init_(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:",self.employee_id)
        print("Salary: ",self.salary)
# Child Class
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print("Department:", self.department)

    def approve_leave(self):
        print(f"{self.name} has approved leave.")

# Creating an object of Manager class
manager1 = Manager(
    name="Rohit",
    age=20,
    employee_id="M111",
    salary=185000,
    department="Operations"
)

# Calling methods
manager1.display_manager_info()
manager1.approve_leave()
