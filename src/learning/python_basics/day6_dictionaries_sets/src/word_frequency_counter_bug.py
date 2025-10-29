"""
Title: Word Frequency Counter (Buggy)
Objective: Show pitfalls when counting words in text.
Date: 2024-06-07
"""

text = input("Enter a sentence: ")

word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print("Word frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
