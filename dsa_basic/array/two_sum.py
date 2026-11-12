"""
nums = [2,7,11,15, 4, 5]
target = 9
"""


def two_sum(nums: list, target: int) -> list:
    rtn = []
    seen = set()
    for ele in nums:
        rem = target - ele
        if rem in seen:
            rtn.append([rem, ele])
        else:
            seen.add(ele)

    return rtn


print(two_sum(nums =[2, 7, 11, 15, 4, 5], target=9))
