from typing import Union
from functools import reduce
from collections.abc import Iterator


def reverse_string(ori: str) -> Union[str, None]:
    return ori[::-1]


def reverse_string_using_reduce(ori: str) -> Union[str, None]:
    rev = reduce(lambda acc, next_char: next_char + acc, ori)
    return rev


def using_reversed_methods(ori: str) -> [str]:
    reversed_str_iter = reversed(ori)
    is_iterator = isinstance(reversed_str_iter, Iterator)
    reversed_str = ''
    if is_iterator:  # it is lazy mean that will not calculate value until required or iterated over
        reversed_str = ''.join(reversed_str_iter)
    return reversed_str


def test_reverse_string():
    assert reverse_string('PINTU') == 'UTNIP'
    assert reverse_string("") == ""
    assert reverse_string('Hello what can be next ?') == '? txen eb nac tahw olleH'
    #  ----------------- using reduce -------------------
    assert reverse_string_using_reduce('PINTU') == 'UTNIP'
    #  ----------------- using reversed -----------------
    assert using_reversed_methods('PINTU') == 'UTNIP'
