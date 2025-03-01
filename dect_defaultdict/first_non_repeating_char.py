"""
Input: "leetcode"
Output: "l"

Input: "aabb"
Output: None

"""

input = "tleetcodel"

for i in range(len(input)):
    if input[i] not in input[i + 1:] + input[0:i - 1]:
        print(f"first non repeating: {input[i]}")
        break

# using dict
fre_count = {}
for char in input:
    if char in fre_count.keys():
        fre_count[char] += 1
    else:
        fre_count[char] = 1

for key, value in fre_count.items():
    if value == 1:
        print(f"non-repeating char is : {key}")
        break

# using defaultdict

from collections import defaultdict

default_dict = defaultdict(int)

for char in input:
    default_dict[char] += 1
for key, value in default_dict.items():
    if value == 1:
        print(f"first non repeating char in using defaultdict: {key}")
        break


# using counter

from collections import Counter

counted = Counter(input)
for char in input:
    if counted[char]==1:
        print(char)
        break
print(f"counter: {dict(counted)}")
