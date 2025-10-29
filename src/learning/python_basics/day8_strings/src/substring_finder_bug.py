"""
Title: Substring Finder (Buggy)
Objective: Highlight case-sensitivity and index mistakes.
Date: 2024-06-07
"""

sentence = input("Enter a sentence: ")
keyword = input("Enter a word to find: ")

position = sentence.find(keyword)

if position:
    print(f"'{keyword}' found at index {position}.")
else:
    print(f"'{keyword}' was not found in the sentence.")
