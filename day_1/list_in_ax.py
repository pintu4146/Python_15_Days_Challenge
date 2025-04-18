"""
Edge Cases:
Empty list ([] should return an error or handle gracefully)
List with one element ([5])
List with all the same numbers ([3, 3, 3])
List with negative numbers ([-10, -5, -1])
List with floating-point numbers ([3.2, 4.5, -2.1])
List with very large numbers ([10^18, -10^18, 10^9])
"""


try:
    # genrating list
    raw_list = input("enter list ele comma seperated")
    if not raw_list:
        raise "Empty list provide"
    input_list = list(map(float, raw_list.strip().split(',')))
    max_list, min_list = max(input_list), min(input_list)
    print(f"max: {max_list}", f"min: {min_list}", sep='\n')
except ValueError as e:
    print(f"ValueError exception occured: {e}")


