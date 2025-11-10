"""
Title: Word Frequency Counter
Objective: Count how often words appear in user-provided text.
Date: 2024-06-07
"""

text = input("Enter a sentence: ")

word_counts = {}
for word in text.lower().split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
