from day_2_utils import print_instructions
"""
🚀 Day 2 – Problem 3: List Operations & Indexing
👉 Problem Statement:

Create a list of fruits: ["Apple", "Banana", "Mango", "Grapes", "Orange"]
Perform the following operations:
Access the first fruit (0th index).
Access the last fruit (negative indexing).
Slice the list to get the middle 3 fruits.
Reverse the list using slicing.
Append "Pineapple" and remove "Banana" from the list.
"""

# list_init = [input("enter string") for i in range(5)]
list_init = ["Apple", "Banana", "Mango", "Grapes", "Orange"]

# Access the first fruit (0th index).
print_instructions("# Access the first fruit (0th index).")
print(list_init[0])
# Access the last fruit (negative indexing).
print(list_init[-1])
# Slice the list to get the middle 3 fruits.
print(list_init[1:5])
# Reverse the list using slicing.
print(list_init[::-1])
# Append "Pineapple" and remove "Banana" from the list.
print_instructions('Append "Pineapple" ')
list_init.append('Pineapple')
print(list_init)
print_instructions('remove "Banana" from the list')
list_init.remove('Banana')
print(list_init)

# ✅ 5️⃣ Insert at Specific Position (Insert "Blueberry" at index 2)

print(f"After Inserting 'Blueberry' at index 2: {list_init}")

# ✅ 6️⃣ Remove by Index (`pop()`)
removed_item = list_init.pop(3)
print(f"Removed Item: {removed_item}")
print(f"List after popping index 3: {list_init}")

# ✅ 7️⃣ Find Index of an Element
index_mango = list_init.index('Mango')
print(f"Index of 'Mango': {index_mango}")

# ✅ 8️⃣ Count Occurrences of an Element
count_apple = list_init.count('Apple')
print(f"Occurrences of 'Apple': {count_apple}")

# ✅ 9️⃣ Sort the List (Alphabetical Order)
sorted_list = sorted(list_init)
print(f"Sorted List: {sorted_list}")

# ✅ 🔟 Reverse Sorting
list_init.sort(reverse=True)
print(f"Reverse Sorted List: {list_init}")

# ✅ 1️⃣1️⃣ Extend List with Another List
more_fruits = ["Strawberry", "Peach"]
list_init.extend(more_fruits)
print(f"After Extending with {more_fruits}: {list_init}")

# ✅ 1️⃣2️⃣ Remove All Elements (`clear()`)
list_init.clear()
print(f"List After Clearing: {list_init}")


# 📌 More Handy List Operations for Developers

fruits = ["Apple", "Banana", "Mango", "Blueberry"]
filtered_fruits = [fruit for fruit in fruits if fruit.startswith('B')]
print(f'filtered_fruits starting with B: {filtered_fruits}')  # ✅ Output: ['Banana', 'Blueberry']

# Flattening Nested Lists

nested_list = [[1, 2], [3, 4], [5, 6]]
copy_nested_list = nested_list[:]

flat_list = [ele for sub_list in nested_list for ele in sub_list]
print(f'original_list : {copy_nested_list}, flattened_list : {flat_list}')  # ✅ Output: [1, 2, 3, 4, 5, 6]

# Finding the Maximum & Minimum

numbers = [10, 25, 5, 40, 60]
print(max(numbers))  # ✅ Output: 60
print(min(numbers))  # ✅ Output: 5


"""
🚀 Summary (Must-Know List Operations)
Operation	                                Code Example	            Use Case
Access First & Last Element	                list[0], list[-1]	        Basic list operations
Slicing	                                           list[1:4]	        Extract sublists
Reversing	                                    list[::-1]	            Useful in backtracking, recursion
Appending	                                    list.append(x)	        Add an item at the end
Removing	                                    list.remove(x)	        Removes first occurrence
Pop by Index	                                list.pop(2)	            Removes & returns element at index
Find Index	                                    list.index(x)	        Find position of an element
Sorting	                                   sorted(list) or list.sort()	Sort list in order
Extend List	                                list.extend(other_list)	    Merge two lists
List Comprehension	                        [x**2 for x in range(5)]	Generate lists efficiently
Filter Items	                        [x for x in list if condition]	Select specific elements
Remove Duplicates	                                list(set(my_list))	Keep unique elements

"""

