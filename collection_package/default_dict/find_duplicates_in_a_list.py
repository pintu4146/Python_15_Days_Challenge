"""
Find Duplicates in a List

Problem statement:

Given a list of integers, write a Python function to identify all duplicate elements.

Input:
nums = [1, 2, 3, 2, 4, 1, 5, 2]



Expected output:
[2, 1]



Requirements:
1. Each duplicate should appear only once in the output.
2. Preserve the order in which duplicates are first detected.
3. Handle an empty list.
4. Handle a list with no duplicates.
Your task: Implement the function without using Counter or sorting.
"""

from collections import defaultdict


def find_duplicates(nums: list) -> list:
    """
:return duplicates ele as list
    :param nums:
    """
    rtn = []
    freq_ele = defaultdict(int)
    for ele in nums:
        freq_ele[ele] += 1
    for ele, freq in freq_ele.items():
        if freq > 1:
            rtn.append(ele)

    return rtn


def duplicates_order(nums: list[int]) -> list[int]:
    """finding the duplicates in their order"""
    seen = set()
    duplicates = []
    for ele in nums:
        if ele in seen and ele not in duplicates:
            duplicates.append(ele)
        else:
            seen.add(ele)
    return duplicates


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 4, 1, 5, 2]
    rtn = find_duplicates(nums)
    rtn_occur = duplicates_order(nums)
    print("maintaining duplicates order", rtn_occur)
    print("without maintaining the order", rtn)
