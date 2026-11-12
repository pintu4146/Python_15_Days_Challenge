"""
Problem statement

Given a string containing words separated by spaces, reverse the order of the words without reversing the individual characters.

Input:
sentence = "Python is awesome"



Expected output:
"awesome is Python"



Additional requirements:
- Handle multiple spaces.
- Handle leading and trailing spaces.
- Handle an empty string.
- Preserve the spelling of individual words.

"""
def reverse_sentace(input_str: str) -> list:
    splt_sent = input_str.split()
    print(splt_sent)
    rev = reversed(splt_sent)

    return " ".join(rev)


print(reverse_sentace("Python is awesome"))