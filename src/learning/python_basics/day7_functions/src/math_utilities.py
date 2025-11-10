"""
Title: Math Utilities
Objective: Provide reusable functions for basic math operations.
Date: 2024-06-07
"""

def square(number: float) -> float:
    """Return the square of the given number."""
    return number ** 2


def cube(number: float) -> float:
    """Return the cube of the given number."""
    return number ** 3


def average(first: float, second: float) -> float:
    """Return the average of two numbers."""
    return (first + second) / 2


value = float(input("Enter a number to square and cube: "))
print(f"Square: {square(value)}")
print(f"Cube: {cube(value)}")

first_value = float(input("Enter the first number to average: "))
second_value = float(input("Enter the second number to average: "))
print(f"Average: {average(first_value, second_value)}")
