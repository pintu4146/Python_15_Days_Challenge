"""
Count Vowels and Consonants

Write a function that takes a string and returns the number of:

Vowels

Consonants

Other characters (digits, punctuation, spaces, etc.)
"""

from typing import Tuple


def count_v_cons(input_str: str) -> Tuple[int, int, int]:
    sanitize_str = input_str.lower()
    total_sum = len(sanitize_str)
    v_list = ['a', 'e', 'i', 'o', 'u']
    v_count, c_count, sp_count = 0, 0, 0
    for char in sanitize_str:
        if char in v_list:
            v_count += 1
        elif char.isalpha():
            c_count += 1
    return v_count, c_count, total_sum - (v_count + c_count)


print(count_v_cons("This is Python 3!"))
