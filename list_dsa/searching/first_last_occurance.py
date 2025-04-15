"""
🎯 Problem: First and Last Occurrence of Target
Given: A sorted array arr and a target value x
Return: The first and last index of x
If not found, return [-1, -1]

🧠 Real-World Examples:
Count frequency in a sorted array

Log search: Find first and last timestamps

Range queries

✅ Example:
python
Copy
Edit
Input: arr = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Input: arr = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
🧩 Intuition:
We run two binary searches:

One to find the first occurrence (left bound)

One to find the last occurrence (right bound)

🔧 Function Signature:
python
Copy
Edit
def first_and_last_occurrence(arr: list[int], target: int) -> list[int]:
    pass
🧪 Test Cases to Add:
python
Copy
Edit
def test_first_and_last_occurrence():
    assert first_and_last_occurrence([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert first_and_last_occurrence([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert first_and_last_occurrence([1, 2, 2, 2, 2, 3, 4], 2) == [1, 4]
    assert first_and_last_occurrence([2, 2, 2, 2], 2) == [0, 3]
    assert first_and_last_occurrence([1], 1) == [0, 0]
    assert first_and_last_occurrence([], 3) == [-1, -1]
    print("✅ first_and_last_occurrence passed all test cases")

"""
from typing import List


def first_occurrence(arr: List[int], target: int, is_last_occur=False) -> int:
    left, right, first_occur, last_occur = 0, len(arr)-1, -1, -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            first_occur = mid
            if is_last_occur:
                left = mid + 1
            else:
                right = mid-1
        elif arr[mid] > target:
            right = right - 1
        else:
            left = left+1
    return first_occur


def first_and_last_occurrence(arr: List[int], target: int) -> List[int]:
    res = first_occurrence(arr, target)
    res_last = first_occurrence(arr, target, is_last_occur=True)
    print(res)
    print(res_last)
    return [res, res_last]


first_and_last_occurrence([5, 7, 7, 8, 8, 10], 8)
def test_first_and_last_occurrence():
    assert first_and_last_occurrence([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert first_and_last_occurrence([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert first_and_last_occurrence([1, 2, 2, 2, 2, 3, 4], 2) == [1, 4]
    assert first_and_last_occurrence([2, 2, 2, 2], 2) == [0, 3]
    assert first_and_last_occurrence([1], 1) == [0, 0]
    assert first_and_last_occurrence([], 3) == [-1, -1]
    print("✅ first_and_last_occurrence passed all test cases")
