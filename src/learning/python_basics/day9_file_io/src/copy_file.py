"""
Title: File Copier
Objective: Copy the contents of one file into another.
Date: 2024-06-07
"""

source_path = input("Enter the source filename: ")
destination_path = input("Enter the destination filename: ")

with open(source_path, "r", encoding="utf-8") as source_file:
    contents = source_file.read()

with open(destination_path, "w", encoding="utf-8") as destination_file:
    destination_file.write(contents)

print("File copy complete.")
