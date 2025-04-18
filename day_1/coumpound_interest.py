"""
Q9: Compound Interest Calculation

Formula: A = P(1 + r/100)^t
Edge Cases:
Zero principal amount
Zero or negative interest rate
Negative time period

"""
from typing import Any

import pytest


def compound_interest(principle: float, rate: float, time: int) -> ValueError | float | Any:
    """

    :param principle: total amount
    :param rate: rate of interest consider year
    :param time: give time in month
    :return: interest
    """
    if time < 0:
        raise ValueError("time cant be in negative")
    if principle <= 0:
        raise ValueError("Principal amount cannot be negative")
    if rate <= 0:
        return principle
    year = time / 12
    interest = principle * (1 + rate / 100) ** year
    return round(interest, 2)


interest_amount = compound_interest(100, 2, 0)
print(round(interest_amount, 2))


# ✅ Test Case 1: Standard case (1 year at 5%)
def test_standard_case():
    assert compound_interest(1000, 5, 12) == 1050.00


# ✅ Test Case 2: Multiple years (2 years at 3%)
def test_multiple_years():
    assert compound_interest(5000, 3, 24) == 5304.50


# ✅ Test Case 3: Zero principal (No money, no interest)
def test_zero_principal():
    assert compound_interest(0, 5, 12) == 0.00


# ✅ Test Case 4: Zero interest rate (Should return principal)
def test_zero_interest():
    assert compound_interest(1000, 0, 12) == 1000.00


# ✅ Test Case 5: Large principal and long duration
def test_large_values():
    assert compound_interest(1000000, 7, 60) == pytest.approx(1402551.31, rel=1e-2)


# ✅ Test Case 6: Negative time period (Should raise ValueError)
def test_negative_time():
    with pytest.raises(ValueError, match="time cant be in negative"):
        compound_interest(1000, 5, -5)


# ✅ Test Case 7: Negative interest rate (Should raise ValueError)
def test_negative_interest():
    with pytest.raises(ValueError, match="time cant be in negative"):
        compound_interest(1000, -5, 12)


# ✅ Test Case 8: Negative principal (Invalid input)
def test_negative_principal():
    with pytest.raises(ValueError, match="Principal amount cannot be negative"):
        compound_interest(-1000, 5, 12)


# ✅ Test Case 9: High precision check
def test_high_precision():
    assert compound_interest(1500.75, 4.25, 36) == pytest.approx(1700.34, rel=1e-2)
