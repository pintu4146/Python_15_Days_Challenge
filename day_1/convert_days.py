"""

👉 Problem Statement:
Convert a given number of days into years, weeks, and remaining days.

📌 Edge Cases to Handle
✅ Standard case (e.g., 365 should be 1 year, 0 weeks, 0 days)
✅ Handling Leap Years? (For simplicity, assume 1 year = 365 days)
✅ Zero days input (0) should return 0 years, 0 weeks, 0 days
✅ Negative input (-10) should raise a ValueError
✅ Large input (10000 days) should be handled correctly
"""
import pytest


def convert_days(days: int) -> str:
    if days < 0:
        raise ValueError('Number of days cannot be negative')
    year = days // 365
    week = (days - (365 * year)) // 7
    day = days - ((year * 365) + week * 7)
    return f"{year} year, {week} weeks, {day} days"


res = convert_days(372)
print(res)


# writing test cases in same file for faster practice and taking help of the GPT for broader test case
def tests_simple():
    assert convert_days(372) == '1 year, 1 weeks, 0 days'


#  Test Cases for pytest
def test_standard_case():
    assert convert_days(365) == (1, 0, 0)


def test_extra_days():
    assert convert_days(372) == (1, 1, 0)


def test_large_input():
    assert convert_days(10000) == (27, 24, 5)


def test_zero_days():
    assert convert_days(0) == (0, 0, 0)


def test_negative_input():
    with pytest.raises(ValueError, match="Number of days cannot be negative"):
        convert_days(-10)
