"""
Title: Sum of Even Numbers (Buggy)
Objective: Emphasize careful range handling in loops.
Date: 2024-06-07
"""

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total = 0
for number in range(start, end):
    if number % 2 == 1:
        total += number

print(f"The sum of even numbers from {start} to {end} is {total}.")
