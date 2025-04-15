"""
🧠 Problem Statement:
You are given a list of names (strings).
Write a Python program to combine all names into a single string, with each name separated by a space.

✅ Example Input:
python
Copy
Edit
names = ["Alice", "Bob", "Charlie"]
✅ Expected Output:
python
Copy
Edit
"Alice Bob Charlie"
📎 Edge Cases:
Empty list → return empty string ""

List with one name → return the name as-is

Names with extra spaces → trim using .strip()

Mixed casing → (optional) normalize with .title() or .lower() if needed


"""
from typing import List


def con_str(names: List[str]) -> str:
    if not names:
        return ""
    rtn = ' '.join(name.strip() for name in names if name)
    return rtn


def test_con_str():
    assert con_str(["Alice", "Bob", "Charlie"]) == 'Alice Bob Charlie'
    assert con_str(["Alice", "Bob     ", "Charlie    "]) == 'Alice Bob Charlie'
    assert con_str(["Alice", "", "Charlie    "]) == 'Alice Charlie' # NOTE: empty string strip will return empty
    assert con_str(["Alice", " ", "Charlie    "]) == 'Alice  Charlie' # NOTE: one or more white spaces return atleast one
    assert con_str([]) == ''

