"""
Title: Write and Read Notes (Buggy)
Objective: Practice fixing file mode and resource handling mistakes.
Date: 2024-06-07
"""

note = input("Write a note to save: ")

notes_file = open("notes.txt", "r", encoding="utf-8")
notes_file.write(note)
notes_file.close()

print("Note saved. Contents of the file:")
print(notes_file.read())
