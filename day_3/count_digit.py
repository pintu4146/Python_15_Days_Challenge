import math


def str_count_digit(num: int) -> int:
    """

    :param num: number that to count digit
    :return : count of the digit
    """
    num = num if num > 0 else -num
    return len(str(num))


def count_digit(num: int) -> int:
    """

    :param num:
    """
    count = 0
    num = num if num > 0 else -num
    while num > 0:
        count += 1
        num //= 10
    return count


# converting the num in str and count
print(str_count_digit(123))

# without coverting to str

print(count_digit(123))


# efficient count digit

def eff_count_digit(num: int) -> float:
    """

    :param num:
    """
    num = num if num > 0 else -num

    return math.floor(math.log10(num)) + 1 if num != 0 else 1


print(eff_count_digit(0))
