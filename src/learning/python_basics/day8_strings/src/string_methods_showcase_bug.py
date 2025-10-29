"""
Title: String Methods Showcase (Buggy)
Objective: Practice correcting string method usage.
Date: 2024-06-07
"""

text = input("Enter a phrase to explore: ")

print(f"Uppercase: {text.to_upper()}")
print(f"Lowercase: {text.toLower()}")
print(f"Title Case: {text.title}")
print(f"Replaced spaces with hyphens: {text.replace(' ', '-')}")
print(f"Stripped whitespace: '{text.strip(' ')}'")
print(f"Length: {text.len()} characters")
