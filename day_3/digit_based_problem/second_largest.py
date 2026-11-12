"""
[10,12,18,20,32]


"""

def second_largest(nums: list) -> int:
    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second






if __name__ =="__main__":
    nums = [10, 12, 18, 20, 32, 32]
    print(second_largest(nums=nums))