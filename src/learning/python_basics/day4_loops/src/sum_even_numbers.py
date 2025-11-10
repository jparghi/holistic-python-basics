"""
Title: Sum of Even Numbers
Objective: Add all even numbers within a user-defined range.
Date: 2024-06-07
"""

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total = 0
for number in range(start, end + 1):
    if number % 2 == 0:
        total += number

print(f"The sum of even numbers from {start} to {end} is {total}.")
