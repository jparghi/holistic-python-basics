"""
Title: Number Operations Showcase (Buggy)
Objective: Illustrate mistakes in arithmetic operations and casting.
Date: 2024-06-07
"""

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {int(first_number) - second_number}")
print(f"Multiplication: {float(first_number) * int(second_number)}")
print(f"Division: {int(first_number) // int(second_number)}")
print(f"Modulus: {int(first_number) % int(second_number)}")
