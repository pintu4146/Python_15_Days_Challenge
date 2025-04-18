"""
✅ Q3: Print a Right-Angled Triangle Pattern of Stars
🧠 Problem Statement:
Write a Python function that:

Accepts an integer n

Prints a right-angled triangle pattern using "*" symbols

"""


def print_right_angles_triangled(x: int) -> str:
    if x<=0:
        return 'entered number should be positive'
    pattern_till_now = []
    for i in range(1, x+1):
        pattern_till_now.append(i * '*'
    )
    return '\n'.join(pattern_till_now)



while True:
    try:
        x = int(input("Enter a number"))
        print(print_right_angles_triangled(x))
        break
    except ValueError as e:
        print("try with number...")


