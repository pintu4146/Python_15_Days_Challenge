"""

Python coding interview – 7 essential problems
1. First non-repeating character
Input: "swiss"

Output: "w"

"""
from collections import defaultdict


def first_non_repeating_char(input_str: str) -> str:
    freq_count = defaultdict(int)
    for ele in input_str:
        freq_count[ele] += 1

    for key, val in freq_count.items():
        if val == 1:
            return key

    return "-1"


if __name__ == "__main__":
    input = "swissw"
    rtn = first_non_repeating_char(input)
    print(rtn)
