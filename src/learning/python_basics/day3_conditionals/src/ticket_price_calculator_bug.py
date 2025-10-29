"""
Title: Ticket Price Calculator (Buggy)
Objective: Highlight logic issues in tiered pricing decisions.
Date: 2024-06-07
"""

age = int(input("Enter your age: "))
member_input = input("Are you a museum member? (yes/no): ")

if age < 5:
    price = 0
elif age <= 17:
    price = 8
elif age >= 65:
    price = 7
else:
    price = 12

if member_input:
    price = price - 20

print(f"Your ticket price is ${price}.")
