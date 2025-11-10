"""
Title: Multiplication Table Printer (Buggy)
Objective: Practice fixing nested loop mistakes.
Date: 2024-06-07
"""

limit = int(input("Show tables up to which number? "))

for base in range(1, limit):
    print(f"\nMultiplication table for {base}")
    for multiplier in range(10):
        product = base * multiplier
        print(f"{base} x {multiplier} = {product}")
