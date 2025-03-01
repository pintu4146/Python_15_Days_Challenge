"""
Q8: Check if a given string is a palindrome
Edge Cases:
Single character string ("a")
Empty string ("")
Strings with spaces ("A man a plan a canal Panama")
Case sensitivity ("Racecar" vs "racecar")
Strings with special characters ("Madam, I'm Adam.")
"""
import re
from collections import deque
#
# try:
#     input_str = input("enter the string for palindrome check")
#
#     # let's clean for the spces and non-alphaNumeric
#     alpha_num = ''
#     if not input_str.isalnum():
#         alpha_num = re.sub('[^A-Za-z0-9]', '', input_str)
#     if not input_str:
#         raise "emptyb list is provide"
#     if alpha_num == alpha_num[::-1]:
#         print(f"palindromic String: {alpha_num}")
#     else:
#         print("not palindromic string")
#
# except ValueError as e:
#     print("value error occured")
# except TypeError as te:
#     print(f"TypeError: {te}")


# two pointer concept
def palindrome_check_two_pointer(string):
    left, right = 0, len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def palindrome_check_deque(cleaned_str):
    init = deque(cleaned_str, maxlen=len(cleaned_str))
    print(init)
    while len(init) > 1:
        if init.popleft()!=init.pop():
            return False
    return True


raw_str = input("Enter the string you want to check:\t")
cleaned_str = re.sub(r'[^A-Z0-9a-z]', '', raw_str)
# two pointer concept
# print(palindrome_check_two_pointer(cleaned_str))

# using python collections deque

print(palindrome_check_deque(cleaned_str))
