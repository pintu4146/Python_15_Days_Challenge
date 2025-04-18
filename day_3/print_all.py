"""
🧠 Problem Statement:
Write a Python function that:

Takes two numbers: start and end

Returns a list of all even numbers in that inclusive range [start, end]
"""

from typing import List


def list_even(start: int, end: int) -> List[int]:
    rtn_list = []
    if start > end:
        return rtn_list
    start = start if start % 2 == 0 else start + 1

    for i in range(start, end + 1, 2):
        rtn_list.append(i)
    return rtn_list


while True:
    try:
        start, end = map(int, input("enter number sapce seperated").split(' '))
        print(f'list of even num: {list_even(start=start, end=end)}')
    except ValueError as e:
        print("Try with space separated INTEGER....")
