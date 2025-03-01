"""Q3: Convert temperature from Celsius to Fahrenheit
Edge Cases:
Edge values like absolute zero (-273.15°C)
Large values (e.g., 10000°C)
Floating-point precision issues (e.g., 36.6666666667°C)
Negative temperatures (e.g., -40°C, which is the same in Fahrenheit)
User enters an invalid input (non-numeric like "thirty")
F = (C × 9/5) + 32
"""
import unittest


def con(temp_cel):
    try:
        # temp_cel = int(input("enter celcious"))
        f = (temp_cel * 9 / 5) + 32
        print(f"value in farenhiet: {f:.2f}")
        return f
    except ValueError:
        print("there is value error ")
    except TypeError as te:
        raise f"type error: {te}"


class MyTest(unittest.TestCase):
    def test_con_success(self):
        self.assertEqual(con(5), 41.0)
