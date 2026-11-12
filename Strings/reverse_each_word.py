"""
give a sentace we have to reverse the earch word of the sentance


input : Python is awesome
output: nohtyP si emosewa
"""


def reverse_word(word) -> str:
    chars = list(word)
    start = 0
    end = len(chars) - 1
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
    return "".join(chars)


def reverse_each_word(sentance: str) -> str:
    return " ".join(reverse_word(word) for word in sentance.split())



print(reverse_each_word("Pintu is Coder"))

print(reverse_each_word("Python is awesome"))
# nohtyP si emosewa

print(reverse_each_word("Hello"))
# olleH

print(reverse_each_word(""))
# ""

print(reverse_each_word("  I   love   coding  "))
# I evol gnidoc