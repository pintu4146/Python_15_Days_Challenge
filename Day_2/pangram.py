"""
✅ Q9: Check if a String is a Pangram
🧠 Problem Statement:
Write a Python program to check whether a given string is a pangram.

A pangram is a sentence that contains every letter of the English alphabet at least once.

✅ Example Input & Output

Input	Is Pangram?
"The quick brown fox jumps over the lazy dog"	✅ Yes
"Hello world"	                                ❌ No
"Pack my box with five dozen liquor jugs"	    ✅ Yes
"""
from typing import Union



def is_pangram(input_str: str) -> Union[bool, None]:
    if not input_str:
        return None
    # return 26 == len(set(ele for ele in input_str.lower() if ord(ele) in range(97, 123)))
    return 26 == len(set(ele for ele in input_str.lower() if ele.isalpha()))


def test_is_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    assert is_pangram('Hello world') == False
    assert is_pangram('Pack my box with five dozen liquor jugs') == True

    # assert is_pangram('"Hello world"') == False
