"""
Problem:
Given a list of integers, return all possible subsets (the power set).

Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""
from typing import List


def get_all_possible_subsets(lst: list) -> List[list]:
    rtn = []
    total_num_subset = 2 ** len(lst)
    for i in range(1, total_num_subset):  # from 1 to remove empty subset
        subset = []
        for j in range(len(lst)):
            if (i >> j) & 1:
                subset.append(lst[j])
        rtn.append(subset)

    return rtn


res = get_all_possible_subsets([1, 2, 3])
print(res)
