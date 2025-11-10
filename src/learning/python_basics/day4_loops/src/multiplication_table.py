"""
Title: Multiplication Table Printer
Objective: Display multiplication tables using nested loops.
Date: 2024-06-07
"""

limit = int(input("Show tables up to which number? "))

for base in range(1, limit + 1):
    print(f"\nMultiplication table for {base}")
    for multiplier in range(1, 11):
        product = base * multiplier
        print(f"{base} x {multiplier} = {product}")
