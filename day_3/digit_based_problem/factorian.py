"""
🔹 3. Strong Number / Factorion
Sum of factorials of its digits equals the number itself.

145 = 1! + 4! + 5! = 145
"""


# def get_factorial_by_digit(digit: int) -> int:
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     return fact


def factorian(num: int) -> bool:
    factorial_look_up = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    return num == sum(factorial_look_up[int(d)] for d in str(num))


while True:
    try:
        print(factorian(int(input('Enter number: '))))
        break
    except ValueError as e:
        print(f"Try with Number: {e}")
