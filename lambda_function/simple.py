def sqr(x: int) -> int:
    """calculates the square of the given integer"""
    return x ** 2


h = lambda x: x ** 2  # not recommended

res = h(3)

print(res)

normal_function = sqr(4)
print(normal_function)

#  lambda in the map function

lst = [i for i in range(10)]

square_of_list = list(map(lambda x: x ** 2, lst))
print(square_of_list)

# filter

even = list(filter(lambda x: x % 2 == 0, lst))
print(even)

# reduce finding the sum
from functools import reduce

reduce_sum = reduce(lambda acc, next: acc + next, lst)
print(reduce_sum)

# finding max from iterables
max_ele = reduce(lambda acc, next: acc if acc > next else next, lst, float('-inf'))

print(max_ele)

# finding min from iterables

min_ele = reduce(lambda acc, next: acc if acc < next else next, lst, float('inf'))

print(min_ele)