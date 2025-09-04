"""

Write a Python program that takes a string as input and returns the most frequent character along with its frequency.
Sample Input:
"This is a sample string"

Sample Output:
Most frequent character: 's', Frequency: 3
"""

from collections import Counter


def most_frequent(input: str) -> str:
    if not input:
        return "string is empty"
    frequency_dict = Counter(list(input))

    max_key = max(frequency_dict, key= frequency_dict.get)
    return f'max_freq for key \'{max_key}\' frequency {frequency_dict.get(max_key)}'


print(most_frequent("This is a sample string"))