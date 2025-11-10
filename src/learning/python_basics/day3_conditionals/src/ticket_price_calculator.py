"""
Title: Ticket Price Calculator
Objective: Determine ticket price based on age and membership status.
Date: 2024-06-07
"""

age = int(input("Enter your age: "))
is_member_input = input("Are you a museum member? (yes/no): ").strip().lower()
is_member = is_member_input == "yes"

if age < 5:
    price = 0
elif age <= 17:
    price = 8
elif age >= 65:
    price = 7
else:
    price = 12

if is_member:
    price *= 0.8

print(f"Your ticket price is ${price:.2f}.")
