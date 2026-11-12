"""
employee class for dict key test
"""

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary= salary



employees = [
    Employee(101, "pin1", 5),
    Employee(102, "pin2", 6),
    Employee(103, "pin3", 7),
    Employee(104, name="pin4", salary=8)


]

# dict comprehension for the id with salary
employees_salary = {
      emp.id: emp.salary for emp in employees if emp.salary > 6
}
print(len(employees_salary), employees_salary, sep=' -----> ')

# trying making the object as the key

employees_name = {
    emp : emp.name for emp in employees
}
print(employees_name)

