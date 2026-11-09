"""
find all permutation of the given number say 123
all permutations are
123
132
213
231
312
321
"""


def all_permutation(num_list: list, idx):
    """

    """

    if idx == len(num_list):
        print(num_list)
        return
    for i in range(idx, len(num_list)):
        num_list[idx], num_list[i] = num_list[i], num_list[idx]
        all_permutation(num_list, idx=idx + 1)
        num_list[idx], num_list[i] = num_list[i], num_list[idx]


num_arr = [1, 2, 3]
all_permutation(num_arr, 0)