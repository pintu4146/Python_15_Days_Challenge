"""
Q2: Calculate the sum of two numbers entered by the user
Edge Cases:
Input validation (non-numeric input like "abc" or special characters)
Negative numbers (e.g., -5 and -10)100000
Floating-point numbers (3.5 and 2.7)
Large integer values that could cause overflow (10**18 + 10**18)
User enters zero (0 + 5)
"""


# n1, n2 = int(input("enter n1")), int(input('enter n2'))
#
# if isinstance(n1, int) and isinstance(n2, int):
#     print(n1 + n2)


class A:
    def show(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()



obj = B()
print(isinstance(obj, A))
