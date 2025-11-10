"""
Title: Line Counter (Buggy)
Objective: Practice handling file errors and counting loops.
Date: 2024-06-07
"""

file_path = input("Enter the filename to count lines: ")

with open(file_path, "r", encoding="utf-8") as text_file:
    line_count = 0
    for line in text_file:
        pass

print(f"The file has {line_count} lines.")
