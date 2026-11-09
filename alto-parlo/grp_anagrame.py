"""

Problem: Given a list of strings, group words that are anagrams of each other. Anagrams contain the same characters with the same frequencies.

Example:
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

from collections import defaultdict


def anagrame_group(str_list: list):
    grp = defaultdict(list)
    for ele in str_list:
        key = "".join(sorted(ele))
        grp[key].append(ele)
    return list(grp.values())


lst = ["eat", "tea", "tan", "ate", "nat", "bat"]

rtn = anagrame_group(anagrame_group(lst))
print(rtn)
