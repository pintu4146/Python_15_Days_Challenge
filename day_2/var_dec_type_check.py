"""
📌 Problem 1: Variable Declaration & Basic Data Types
👉 Problem Statement:
Create variables to store:

A person's name (string)
A person's age (integer)
A person's average test score (float)
✅ You need to:

Print each variable with its type using type().
Ensure input validation (i.e., age must be an integer, test score a float).
"""


class Person:
    avg_test_score = float(90.1)
    age = int(10)
    name = "pin"


print(f"avg_test_score: {type(Person.avg_test_score)}, "
      f"age: {type(Person.age)}, name: {type(Person.name)}")


# lets take input fromm user

def get_student_details():

    try:
        name = str(input("enter students name")).strip()
        age = int(input("Enter the age in integer"))
        avg_marks = float(input("enter the avg marks in float"))
        return {"name": {"var": name, "type": type(name)},
                "age": {"var": age, "type": type(age)},
                "avg_marks": {"var": avg_marks, "type": type(avg_marks)}}
    except ValueError as te:
        print(f"Value error occurred: {te}")
    except Exception as e:
        print(f"Unknown exception occurred: {e}")


print(get_student_details())


