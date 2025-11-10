"""
Title: Palindrome Checker (Buggy)
Objective: Practice debugging normalization and comparisons.
Date: 2024-06-07
"""

text = input("Enter a word or phrase: ")
normalized = text.replace(" ", "")

if normalized == normalized[1:]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
