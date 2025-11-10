"""
Title: Mini Story Generator (Buggy)
Objective: Highlight common formatting errors when building a story string.
Date: 2024-06-07
"""

character = input("Name a main character: ")
setting = input("Where does the story take place? ")
activity = input("What is the character doing? ")

story = "Once upon a time, {character} visited {setting} and decided to {activity}. "
story += "It was the beginning of a legendary adventure!"

print("Here is your story:")
print(story.upper)
