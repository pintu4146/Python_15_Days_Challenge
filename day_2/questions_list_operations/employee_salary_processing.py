"""
🚀 Medium-Level Problem: Employee Salary Processing
👉 Problem Statement:
You are given a list of employees with:

Employee ID (integer)
Name (string)
Department (string)
Salary (float)
Status ("Active" or "Inactive")
✅ Your Tasks:

1. Filter out inactive employees
2. Sort active employees by salary in descending order
3. Find the highest-paid employee in each department
4. Calculate the average salary for active employees
--------
✅ Example Input:

employees = [
    (1, "Alice", "Engineering", 90000, "Active"),
    (2, "Bob", "Marketing", 75000, "Inactive"),
    (3, "Charlie", "Engineering", 120000, "Active"),
    (4, "David", "HR", 60000, "Active"),
    (5, "Eve", "Marketing", 80000, "Active"),
    (6, "Frank", "Engineering", 110000, "Active"),
    (7, "Grace", "HR", 70000, "Inactive")
]
✅ Expected Output:

# Active Employees Sorted by Salary
[
    (3, "Charlie", "Engineering", 120000, "Active"),
    (6, "Frank", "Engineering", 110000, "Active"),
    (1, "Alice", "Engineering", 90000, "Active"),
    (5, "Eve", "Marketing", 80000, "Active"),
    (4, "David", "HR", 60000, "Active")
]

# Highest-Paid Employee in Each Department
{
    "Engineering": ("Charlie", 120000),
    "Marketing": ("Eve", 80000),
    "HR": ("David", 60000)
}

# Average Salary of Active Employees: 92000.0
⏳ Expected Complexity Analysis
Operation	Time Complexity
Filtering Active Employees	O(N)
Sorting by Salary	O(N log N)
Finding Highest Salary per Department	O(N)
Calculating Average Salary	O(N)
✅ Final Complexity: O(N log N) (Dominated by sorting)
"""

employees = [
    (1, "Alice", "Engineering", 90000, "Active"),
    (2, "Bob", "Marketing", 75000, "Inactive"),
    (3, "Charlie", "Engineering", 120000, "Active"),
    (4, "David", "HR", 60000, "Active"),
    (5, "Eve", "Marketing", 80000, "Active"),
    (6, "Frank", "Engineering", 110000, "Active"),
    (7, "Grace", "HR", 70000, "Inactive")
]


# 1. Filter out inactive employees
print([ep for ep in employees if ep[4] == 'Inactive'])

# 2. Sort active employees by salary in descending order
