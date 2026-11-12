"""


nums = [1,2,3,0, 4,0 ]  edge = 0
output = [24,12,8,6]



"""

def product_of_ele(nums: list) -> list:
    prod = 1
    res = []
    count =0
    index_zero = 0
    for idx, ele in enumerate(nums):
        if ele ==0:
            count +=1
            index_zero = idx

    if count >1:
        return [0]* (len(nums))
    if count ==0:

        for ele in nums:
            prod *= ele
        for ele in nums:
            res.append(prod//ele)
        return res
    if count ==1:
        prod_1 = 1
        for idx, ele in enumerate(nums):
            if idx != index_zero:
                prod_1 *= ele
        rtn = [0] *(len(nums))
        rtn[index_zero] = prod_1
        return rtn
    return []




nums = [1,2,3,4,0 ]
print(product_of_ele(nums))