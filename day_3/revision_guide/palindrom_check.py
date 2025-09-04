"""
Problem Statement:

Write a Python program to check whether a given number is a palindrome (i.e., it reads the same forward and backward).

"""
from typing import Any


def is_palindrom(input: str | int) -> bool | int | Any:
    if isinstance(input, str):
        return input == input[::-1]
    elif isinstance(input, int):
        reverse, ori_input = 0, input
        while input > 0:
            reverse = reverse * 10 + input % 10
            input //= 10
        return reverse == ori_input
    else:
        return "supported arg is int and str as of now"


print(is_palindrom(121))

# input_example = '121'
# print(is_palindrom(input_example))
