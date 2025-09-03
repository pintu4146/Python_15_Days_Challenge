"""

You are given an array of size n-1 containing distinct integers in the range 1 to n.
The array is unsorted and exactly one number is missing from this range.

Task:
Write a Python function to find and return the missing number.

Constraints:

1 <= n <= 10^6

Array length = n - 1

All elements are unique and within the range [1, n].
"""
from typing import List


def finding_missing_num_range(arr: List[int], n) -> int:
    """

    :param arr: list of integer with distinct number
    :param n:
    """
    sum_n_consecutive_num = n * (n+1)//2
    sum_arr_ele = sum(arr)
    return sum_n_consecutive_num - sum_arr_ele

arr = [1,2,3,5]
n =5
print(finding_missing_num_range(arr=arr, n=n))