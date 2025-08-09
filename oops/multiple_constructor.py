"""
Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
"""

class Employee:
    def __init__(self, name: str = None, emp_id: int = None, department: str = None):
        self._name = name
        self._emp_id = emp_id
        self._department = department

    def display_employee(self):
        print(f'emp name= {self._name} emp_id is {self._emp_id} and department: {self._department}')

    def __repr__(self):
        return (f"Employee id: {self._emp_id if self._emp_id  else 'NA'}, "
                f"name: {self._name}, department: {self._department}")


emp = Employee('pintu', '5191', department='Enterprise')
emp_department = Employee(department='ds')

print(emp)
print(emp_department)
