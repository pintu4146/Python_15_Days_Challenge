"""
🔹 4. Perfect Number
Sum of proper divisors (excluding itself) equals the number.

28 → divisors: 1, 2, 4, 7, 14 → sum = 28
"""
from typing import List


def get_divisor(num: int) -> List[int]:
    # since excluding itself so we can save number of iteration
    divisor_list = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisor_list.append(i)
            if num//i != num:
                divisor_list.append(num//i)

    print(sorted(divisor_list))
    return sorted(divisor_list)


def is_perfect_number(num: int) -> bool:
    return num == sum(get_divisor(num))


while True:
    try:
        num = int(input("Enter Number: "))
        print(is_perfect_number(num))
        break
    except ValueError as ve:
        print(f"try with number instead: {ve}")
