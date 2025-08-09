def reverse_numbers(num: int) -> int:
    """

    :param num:
    """
    # 123 -> 321
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10



print(reverse_numbers(num=num))