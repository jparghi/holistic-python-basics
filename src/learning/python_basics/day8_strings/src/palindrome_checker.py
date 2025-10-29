"""
Title: Palindrome Checker
Objective: Determine whether a phrase reads the same forwards and backwards.
Date: 2024-06-07
"""

text = input("Enter a word or phrase: ")
normalized = "".join(char.lower() for char in text if char.isalnum())

if normalized == normalized[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
