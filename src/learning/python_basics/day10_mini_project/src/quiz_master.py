"""
Title: Quiz Master
Objective: Conduct a short quiz and track the user's score.
Date: 2024-06-07
"""

questions = {
    "What keyword defines a function in Python?": "def",
    "Which data type is used to store True or False?": "bool",
    "What symbol starts a comment?": "#",
}

score = 0

for prompt, answer in questions.items():
    user_answer = input(f"{prompt} ").strip().lower()
    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Oops! The correct answer was '{answer}'.\n")

print(f"You scored {score} out of {len(questions)}.")
