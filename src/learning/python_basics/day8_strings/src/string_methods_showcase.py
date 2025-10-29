"""
Title: String Methods Showcase
Objective: Demonstrate common string transformations and formatting.
Date: 2024-06-07
"""

text = input("Enter a phrase to explore: ")

print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")
print(f"Replaced spaces with hyphens: {text.replace(' ', '-')}")
print(f"Stripped whitespace: '{text.strip()}'")
print(f"Length: {len(text)} characters")
