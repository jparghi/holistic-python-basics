"""
Title: Mini Story Generator
Objective: Combine user-supplied words into a playful story using f-strings.
Date: 2024-06-07
"""

character = input("Name a main character: ")
setting = input("Where does the story take place? ")
activity = input("What is the character doing? ")

story = (
    f"Once upon a time, {character} visited {setting} and decided to {activity}. "
    f"It was the beginning of a legendary adventure!"
)

print("Here is your story:")
print(story)
