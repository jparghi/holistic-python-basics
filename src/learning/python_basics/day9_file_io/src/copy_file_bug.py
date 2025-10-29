"""
Title: File Copier (Buggy)
Objective: Highlight errors when copying file contents.
Date: 2024-06-07
"""

source_path = input("Enter the source filename: ")
destination_path = input("Enter the destination filename: ")

source_file = open(source_path, "w", encoding="utf-8")
contents = source_file.read()
source_file.close()

destination_file = open(destination_path, "r", encoding="utf-8")
destination_file.write(contents)
destination_file.close()

print("File copy complete.")
