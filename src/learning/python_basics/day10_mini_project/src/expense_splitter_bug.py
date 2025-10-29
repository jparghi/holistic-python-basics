"""
Title: Expense Splitter (Buggy)
Objective: Provide division and validation errors for debugging.
Date: 2024-06-07
"""

def calculate_share(total: float, people: int) -> float:
    """Return the amount each person should contribute."""
    return total * people


total_cost = float(input("Enter the total expense: $"))
participant_count = int(input("How many people are sharing the cost? "))

if participant_count <= 0:
    print("Each person should contribute: $0.00")
else:
    share = calculate_share(total_cost, participant_count)
    print(f"Each person should contribute: ${share}")
