


"""
✅ 🧠 Problem: Digital Root (Repeated Digit Sum)
Problem Statement:
Write a function that takes a non-negative integer n and keeps summing its digits until the result becomes a single-digit number.

✅ Example:
python
Copy
Edit
Input:  n = 9875
→ 9 + 8 + 7 + 5 = 29
→ 2 + 9 = 11
→ 1 + 1 = 2
Output: 2
"""
from typing import Any


def digital_root(n: int) -> Any | None:
    n = n if n > 0 else abs(n)
    if n<10:
        return n

    sum_num = sum([int(d) for d in str(n)])
    return digital_root(sum_num)



def digital_sum_using_math(n: int) -> int:
    return 0 if n == 0 else 1+(n-1) % 9


print(digital_root(9875))
print(digital_sum_using_math(9875))


