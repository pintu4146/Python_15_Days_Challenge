"""
 Problem Statement:
Write a Python function that:

Takes an integer n

Checks if the number is a Harshad Number

A Harshad Number is divisible by the sum of its digits.
"""


def is_harshed_number(num: int) -> bool:
    if num < 0:
        raise ValueError("provide positive integer")
    if num == 0:
        return True
    return num % sum(int(d) for d in str(num)) == 0


while True:
    try:
        num = int(input())
        print(is_harshed_number(num))
    except ValueError as ve:
        print(f"value error occured ay be you should try with Integer: {ve}")
