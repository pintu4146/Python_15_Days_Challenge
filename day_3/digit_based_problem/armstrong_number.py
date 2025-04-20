"""
 1. Armstrong Number (Narcissistic Number)
A number is Armstrong if the sum of its digits raised to the power of the number of digits equals the number itself.
"""


def is_armstrong_number(n: int) -> bool:
    return n == sum([int(d) ** len(str(n)) for d in str(n)])
    # good for shorter data but since list will create in the emory


# optimised

def is_arm_num_optimised(n: int) -> bool:
    num_digit = len(str(n))
    return n == sum(int(d)**num_digit for d in str(n))
    # due to generator expression not function



while True:
    try:
        num = int(input("Enter Number"))
        print(is_armstrong_number(num))
        print('optimised')
        print(is_arm_num_optimised(num))
        break
    except ValueError as e:
        print(f'enter number {e}')




"""
🔁 Generator Expressions in Python – Detailed Note

What is a Generator Expression?
-------------------------------
A generator expression is a concise way to create a **lazy iterable (generator object)** 
without the need to write a full generator function using `def` + `yield`.

Syntax:
-------
    (expression for item in iterable if condition)

Example:
--------
    squares = (x**2 for x in range(5))
    print(next(squares))  # Output: 0
    print(next(squares))  # Output: 1

Key Properties:
---------------
1. ✅ **Lazy Evaluation** – Generates values one at a time and only when needed.
2. ✅ **Memory Efficient** – Does NOT store the entire result in memory.
3. ✅ **Readable and Compact** – Ideal for single-pass computations.
4. ⚠️ **One-time use** – Generators can be iterated only once.

Use Cases:
----------
- With built-in functions like:
    - `sum()`
    - `max()`
    - `min()`
    - `any()`
    - `all()`
- When processing large datasets or streams
- Avoiding temporary lists for performance

Comparison:
-----------
List Comprehension:
    [x**2 for x in range(5)] → builds and stores the whole list in memory.

Generator Expression:
    (x**2 for x in range(5)) → yields one value at a time as needed.

When NOT to use:
----------------
- If you need to iterate over the results **multiple times**, use list comprehension instead.
- If you're doing complex multi-step iteration, prefer `def` + `yield`.

Example in Context (Armstrong Number):
--------------------------------------
    num_digit = len(str(n))
    is_armstrong = n == sum(int(d)**num_digit for d in str(n))

    # The generator (int(d)**num_digit for d in str(n)) creates one digit's power at a time.

Built-in Functions that Work Well with Generators:
--------------------------------------------------
- `sum()`
- `max()`, `min()`
- `sorted()` (it will consume the generator and create a list)
- `any()`, `all()`
- `enumerate()`, `zip()`, `map()`, `filter()` (all return lazy iterables too!)

Conclusion:
-----------
Generator expressions are a Pythonic, efficient way to process data lazily.
They're perfect when:
- You don't need to store all results
- You want better performance
- You’re using helper functions that consume iterables

"""

