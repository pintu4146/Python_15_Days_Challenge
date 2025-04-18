"""
🧠 Problem Statement:
Write a Python function that:

Accepts an integer n

Returns "Even" if the number is even, "Odd" if it is odd



"""


def even_odd(x: int) -> bool:
    return True if x % 2 == 0 else False


while True:
    try:
        x = int(input("Enter a number"))
        print(f'is_even: {even_odd(x)}')
        break
    except ValueError as e:
        print("Type error occurred try again with INTEGER ..")
