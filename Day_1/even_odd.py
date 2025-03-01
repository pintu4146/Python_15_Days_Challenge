"""
Q6: Write a program to check if a number is even or odd
Edge Cases:
Negative numbers (-2, -3)
Zero (0 should be even)
Large numbers (10^18)
Non-integer values (2.5 should raise an error)
String inputs ("four" should not be allowed)
"""
try:
    num = int(input("enter a number INTEGER"))
    if not isinstance(num,int):
        raise ValueError("try with interger value")
    else:
        if (num & 1) == 0:
            print(f"Number: {num} is EVEN")
        else:
            print(f"Number: {num} is odd")
except ValueError as ve:
    print(f"value error try again: {ve}")
