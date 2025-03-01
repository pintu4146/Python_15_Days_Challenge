"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""
input= ['eat', "tea", "tan", "ate", "nat", "bat"]

print(input)
input_list = ['eat', "tea", "tan", "ate", "nat", "bat"]

print("Input:", input_list)

res = []
processed = set()  # To track words that are already grouped

for ele in input_list[:]:  # Iterate over a copy to avoid modifying the list during iteration
    if ele in processed:
        continue  # Skip words that are already grouped

    in_res = []
    for in_ele in input_list:
        if sorted(ele) == sorted(in_ele):  # Check if anagrams
            in_res.append(in_ele)
            processed.add(in_ele)  # Mark as processed

    res.append(in_res)  # Append the anagram group

print("Output:", res)


#  using dict

from collections import defaultdict


default_dict = defaultdict(list)
#
# for ele in input_list:
#     