"""
Title: Write and Read Notes
Objective: Demonstrate writing to and reading from a text file.
Date: 2024-06-07
"""

note = input("Write a note to save: ")

with open("notes.txt", "w", encoding="utf-8") as notes_file:
    notes_file.write(note + "\n")

print("Note saved. Contents of the file:")
with open("notes.txt", "r", encoding="utf-8") as notes_file:
    print(notes_file.read())
