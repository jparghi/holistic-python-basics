"""
Title: Line Counter
Objective: Count the number of lines in a text file.
Date: 2024-06-07
"""

file_path = input("Enter the filename to count lines: ")

try:
    with open(file_path, "r", encoding="utf-8") as text_file:
        line_count = sum(1 for _ in text_file)
    print(f"The file has {line_count} lines.")
except FileNotFoundError:
    print("The specified file was not found.")
