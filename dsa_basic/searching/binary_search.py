"""
Problem 1: Binary Search (Iterative)
Given a sorted array arr and a target value, return the index of the target if found. Otherwise, return -1.

Function signature:

python

def binary_search(arr: list[int], target: int) -> int:
    pass
Example:

python

Input: arr = [1, 3, 5, 7, 9], target = 7
Output: 3
Constraints:

Use the iterative approach (not recursion)

Time complexity must be O(log n)


"""


def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    # arr must be sorted
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def test_binary_search():
    # Basic cases
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4
    assert binary_search([1, 3, 5, 7, 9], 4) == -1  # Not present

    # Edge cases
    assert binary_search([], 1) == -1  # Empty list
    assert binary_search([10], 10) == 0  # One element
    assert binary_search([10], 5) == -1
    assert binary_search([2, 4], 2) == 0  # Two elements
    assert binary_search([2, 4], 4) == 1
    assert binary_search([2, 4], 3) == -1

    # Large input
    arr = list(range(0, 1000000, 2))  # even numbers
    assert binary_search(arr, 786432) == arr.index(786432)
    assert binary_search(arr, 786431) == -1  # Odd number not present

    print("✅ binary_search passed all test cases")
