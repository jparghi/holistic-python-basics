"""
Title: Logic Truth Table Explorer (Buggy)
Objective: Show logical operator mistakes for debugging practice.
Date: 2024-06-07
"""

values = [True, False]

print("AND results:")
for left in values:
    for right in values:
        print(f"{left} and {right} -> {left & right}")

print("\nOR results:")
for left in values:
    for right in values:
        print(f"{left} or {right} -> {left and right}")

print("\nNOT results:")
for value in values:
    print(f"not {value} -> {value}")
