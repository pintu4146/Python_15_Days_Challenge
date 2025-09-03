import random

# ['a','b','c','r','a']
random_strng = ['a', 'b', 'c', 'r', 'a']
from collections import defaultdict


def get_freq(random_string: list) -> dict:
    """return frequency of the list """
    default_dict = defaultdict(int)
    for char in random_string:
        default_dict[char] += 1

    return dict(default_dict)


print(f'feq: {get_freq(random_strng)}')


class A:
    def __init__(self):
        print("Hello world")


class B(A):
    def __init__(self):
        print("Hello universe")
        super().__init__()


class C(B):
    def __init__(self):
        print("Hello")
        super().__init__()


obj = C()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def get_uniq(list_num: list) -> list:
    look_up = set()
    res = []
    for num in list_num:
        if num not in look_up:
            look_up.add(num)
            res.append(num)
    return res


print(f'unique: {get_uniq(nums)}')
