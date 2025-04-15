"""
🧠 Problem Statement:
Write a Python program that takes the radius of a circle as input, and calculates:

Area of the circle

Circumference of the circle
"""
import math
from typing import Tuple


def get_area_and_circumference(radius: float) -> Tuple:
    pi = math.pi
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return round(area, 2), f'{circumference}.2f'


def test_area_and_circumference():
    assert get_area_and_circumference(5) == (78.54, 31.42)
