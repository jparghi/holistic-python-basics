"""
Title: Greeting Functions
Objective: Demonstrate functions with parameters and default values.
Date: 2024-06-07
"""

def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def personalized_greet(name: str, hobby: str = "learning Python") -> str:
    """Return a message that includes the person's hobby."""
    return f"Hi, {name}. I heard you enjoy {hobby}."


user_name = input("What is your name? ")
print(greet(user_name))

user_hobby = input("What is your favorite hobby? ")
print(personalized_greet(user_name, user_hobby))
