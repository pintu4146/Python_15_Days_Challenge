"""
Q4: Calculate the area of a rectangle given its length and width
Edge Cases:
Zero or negative values (0, 5 or -3, 4 should be invalid)
Floating-point numbers (2.5, 4.1)
Very large numbers (10^9, 10^9)
Non-numeric input (e.g., "five", "six" should raise an error)
"""
try:
    l, b = map(float, input("inter length and breadth comma seperated").strip().split(','))

    if l <= 0 or b <= 0:
        raise ValueError("this input is not exceptable ")

    else:
        MOD = 10 ** 9 + 7
        area = (l * b) % MOD
        print(area)
except Exception as e:
    print(f"there ay be value error: {e}")
