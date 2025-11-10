"""
Title: Logic Truth Table Explorer
Objective: Display how boolean operators behave with different inputs.
Date: 2024-06-07
"""

values = [True, False]

print("AND results:")
for left in values:
    for right in values:
        print(f"{left} and {right} -> {left and right}")

print("\nOR results:")
for left in values:
    for right in values:
        print(f"{left} or {right} -> {left or right}")

print("\nNOT results:")
for value in values:
    print(f"not {value} -> {not value}")
