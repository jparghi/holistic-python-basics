"""
Title: Number Operations Showcase
Objective: Demonstrate how different arithmetic operators work on user-provided numbers.
Date: 2024-06-07
"""

raw_first = input("Enter the first number: ")
raw_second = input("Enter the second number: ")

first_number = float(raw_first)
second_number = float(raw_second)

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Floor Division: {first_number // second_number}")
print(f"Exponent: {first_number ** second_number}")
print(f"Modulus: {first_number % second_number}")
