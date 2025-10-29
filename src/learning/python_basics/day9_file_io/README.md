# Day 9 – File I/O

## 🎯 Learning Goals
- Open files safely using context managers.
- Read from and write to text files.
- Handle file paths and ensure resources are closed properly.

## 📘 Concept Overview
File input and output let programs persist data. Day 9 teaches how to create files, append content, and read data back. You will practice using `with open(...)` to manage resources automatically and learn how to handle missing files gracefully.

## 💻 Example Programs (Python)
1. `write_read_notes.py` – writes notes to a file and reads them back.
2. `copy_file.py` – copies the contents of one file to another using context managers.
3. `count_file_lines.py` – counts the number of lines in a text file.

## 🪲 Bug-Fix Exercises
- `write_read_notes_bug.py`: Fix issues with file modes and missing closures.
- `copy_file_bug.py`: Repair file handling mistakes that lose data.
- `count_file_lines_bug.py`: Correct counting logic and error handling.

## 🧠 Practice Challenges
- Append user reflections to a daily journal file.
- Create a script that backs up a file with a timestamped filename.
- Read a CSV file and print each row in a formatted way.

## 🧘 Reflection Questions
- Why are context managers recommended for file operations?
- What differences exist between read, write, and append modes?
- How can you guard against missing or unreadable files?
