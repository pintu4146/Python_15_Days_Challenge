"""
📌 Problem Statement: Filter and Process a List of Transactions
👉 You are given a list of transactions (in tuples) containing:

Transaction ID (integer)
User Name (string)
Amount (float)
Status (string: "Success", "Failed", "Pending")
✅ Your Task:

1. Filter out failed transactions.
2. Sort the successful transactions by amount (ascending).
3. Remove duplicate transactions (same Transaction ID).
4. Extract only the user names of successful transactions into a new list.
✅ Example Input:

transactions = [
    (101, "Alice", 250.75, "Success"),
    (102, "Bob", 500.00, "Failed"),
    (103, "Charlie", 125.60, "Success"),
    (104, "Alice", 300.50, "Pending"),
    (105, "Bob", 500.00, "Success"),
    (101, "Alice", 250.75, "Success")  # Duplicate transaction
]
✅ Expected Output:

[
    (103, "Charlie", 125.60, "Success"),
    (101, "Alice", 250.75, "Success"),
    (105, "Bob", 500.00, "Success")
]
["Charlie", "Alice", "Bob"]
"""
from typing import List
transactions = [
    (101, "Alice", 250.75, "Success"),
    (102, "Bob", 500.00, "Failed"),
    (103, "Charlie", 125.60, "Success"),
    (104, "Alice", 300.50, "Pending"),
    (105, "Bob", 500.00, "Success"),
    (101, "Alice", 250.75, "Success")  # Duplicate transaction
]


def filter_failed_transactions(arr: List) -> List:
    failed_transactions = [transaction for transaction in arr if transaction[3] == "Failed"]
    print("Filter out failed transactions.")
    print(failed_transactions)
    return failed_transactions


def sort_success_transaction_amount(transactions):
    filtered_success = set([transaction for transaction in transactions if transaction[3] == "Success"])
    # casted into set for unique success transactions
    sorted_transaction_by_amount = sorted(filtered_success, key=lambda transaction: transaction[2])
    # default is in ascending , sorting will on the key for every element of list which is tuple and tuple third \
    # elemmet is amount

    print(sorted_transaction_by_amount)


def user_name_success_transaction(transactions):
    filtered_success_with_user_name = set([transaction[1] for transaction in transactions if transaction[3] == "Success"])
    # casted into set for unique success transactions
    print(filtered_success_with_user_name)


if __name__ == '__main__':
    # Filter out failed transactions.
    filter_failed_transactions(transactions)
    # 2. Sort the successful transactions by amount (ascending).
    sort_success_transaction_amount(transactions)

    # 3. Remove duplicate transactions (same Transaction ID).
    print(set(transactions))

    # Extract only the user names of successful transactions into a new list.
    user_name_success_transaction(transactions)

