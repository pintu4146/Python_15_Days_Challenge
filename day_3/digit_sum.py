"""

🧠 Problem Statement:
Write a Python function that:

Takes an integer n as input

Returns the sum of its digits


"""


def digit_sum(n: int) -> int:
    n = n if n > 0 else abs(n)
    digi_sum = 0
    while n > 0:
        digi_sum += n % 10
        n //= 10
    return digi_sum


def digit_str_sum(n: int) -> int:
    return sum([int(digit) for digit in str(abs(n))])


try:
    n = int(input("enter num"))
    digit_sum(n)
except ValueError as e:
    print(f"Try with integer..: {e}")
