"""
Title: Substring Finder
Objective: Locate a keyword within a sentence and report its position.
Date: 2024-06-07
"""

sentence = input("Enter a sentence: ")
keyword = input("Enter a word to find: ")

position = sentence.lower().find(keyword.lower())

if position != -1:
    print(f"'{keyword}' found at index {position}.")
else:
    print(f"'{keyword}' was not found in the sentence.")
