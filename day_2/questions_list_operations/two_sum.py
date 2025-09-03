# Find two numbers that sum to target (Two Sum)
from typing import List, Union, Tuple


def two_sum(arr: list, target: int):
    """

    :param arr:
    :param target:
    :return:
    """
    look_up = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                return arr[i], arr[j]
    return -1


arr = [5,1, 2, 3, 4, 5]
target = 10

print(two_sum(arr, target))

# optimise it

def optimise_two_sum(arr: List[int], target: int ) -> Union[Tuple[int, int], int]:
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        print(seen)
        if num in seen:
            return complement, num
        seen[num] = i

    return -1

print(optimise_two_sum(arr, 10))



