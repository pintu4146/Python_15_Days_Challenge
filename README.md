# 📌 Python 15 Days Challenge 🚀

Welcome to the **Python 15 Days Challenge Repository!** This repository is a structured learning initiative where we solve **one Python problem per day**, refining our problem-solving skills while focusing on **edge cases, optimization, and best coding practices**. 

## 🌟 **About the Challenge**
- The challenge follows a structured **15-day roadmap** covering **basic to advanced** Python concepts.
- Problems are sourced from **real-world applications, coding interviews, and algorithmic challenges**.
- Each solution is refined through **peer review, optimizations, and deep discussions**.

---

## 📖 **What’s Inside?**
Each day covers **multiple Python topics** with **edge-case handling, performance analysis, and alternative approaches**.

| 📅 **Day** | 📝 **Topics Covered** | 🚀 **Key Learnings** |
|------------|------------------|------------------|
| **Day 1**  | Basics & Input Handling | Print, Input Validation, Exception Handling |
| **Day 2**  | Variables & Data Types | Lists, Strings, Data Conversion |
| **Day 3**  | Conditional Statements & Loops | If-Else, Loops, Nested Conditions |
| **Day 4**  | Functions & Scope | Function Definitions, Recursion, Lambda |
| **Day 5**  | Strings & Regex | String Manipulation, Regular Expressions |
| **Day 6**  | Lists & Tuples | List Comprehensions, Tuple Operations |
| **Day 7**  | Dictionaries & Sets | Hash Tables, Set Operations, Lookups |
| **Day 8**  | File Handling | Reading & Writing Files, CSV & JSON Handling |
| **Day 9**  | Object-Oriented Programming (OOP) | Classes, Inheritance, Encapsulation |
| **Day 10** | Advanced OOP | Abstract Classes, Multiple Inheritance |
| **Day 11** | NumPy Basics | Array Operations, Broadcasting |
| **Day 12** | Pandas for Data Analysis | DataFrames, Data Cleaning |
| **Day 13** | Data Visualization | Matplotlib, Seaborn |
| **Day 14** | Data Cleaning & Preprocessing | Handling Missing Values, Feature Scaling |
| **Day 15** | Machine Learning Basics | Train-Test Split, Model Evaluation |

---

## ✅ **How We Prepare**
This repository follows a structured approach:
1. **Understanding the Problem**  
   - Read the question and identify the **core concept** it aims to teach.
   - Analyze **edge cases** (invalid input, large numbers, negative values, etc.).

2. **Writing the First Solution**  
   - Implement an **initial version** using Python best practices.
   - Ensure it **works for common inputs**.

3. **Code Optimization & Performance Analysis**  
   - Compare **different approaches** (brute force, optimized, alternative solutions).
   - Use **Big-O notation** to analyze efficiency.

4. **Testing & Debugging**  
   - Implement **unit tests (`unittest` & `pytest`)** for validation.
   - Catch **runtime exceptions, incorrect logic, and edge cases**.

5. **Deep Dives into Related Concepts**  
   - If a problem involves **recursion, OOP, `collections.deque`**, we do a **comprehensive study**.
   - Real-world applications of Python **(caching, AI, finance, web scraping, etc.)**.

---

## 🔥 **Sample Problems & Solutions**
### 📌 **Sliding Window Maximum (Optimized O(N) Solution)**
```python
from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
