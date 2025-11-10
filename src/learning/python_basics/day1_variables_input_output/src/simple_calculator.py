"""
Title: Simple Calculator
Objective: Perform basic arithmetic using two user-provided numbers.
Date: 2024-06-07
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"Sum: {first_number + second_number}")
print(f"Difference: {first_number - second_number}")
print(f"Product: {first_number * second_number}")
if second_number != 0:
    print(f"Quotient: {first_number / second_number}")
else:
    print("Quotient: Undefined (division by zero)")
