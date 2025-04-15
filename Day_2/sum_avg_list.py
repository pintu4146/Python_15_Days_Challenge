from typing import List, Union, Optional


# numbers =


# finding sum and avg

def find_avg(numbers: List[int]) -> Optional[float]:
    sum_arr = sum(numbers) # order of (n)
    len_arr = len(numbers) # order of (1)
    return sum_arr/len_arr if len_arr > 0 else None


def test_find_avg():
    assert find_avg([10, 20, 30, 40, 50]) == 30.0
    assert find_avg([]) is None

