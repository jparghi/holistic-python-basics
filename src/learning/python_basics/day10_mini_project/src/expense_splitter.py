"""
Title: Expense Splitter
Objective: Split a total expense evenly among participants.
Date: 2024-06-07
"""

def calculate_share(total: float, people: int) -> float:
    """Return the amount each person should contribute."""
    return round(total / people, 2)


total_cost = float(input("Enter the total expense: $"))
participant_count = int(input("How many people are sharing the cost? "))

if participant_count <= 0:
    print("The number of people must be greater than zero.")
else:
    share = calculate_share(total_cost, participant_count)
    print(f"Each person should contribute: ${share:.2f}")
