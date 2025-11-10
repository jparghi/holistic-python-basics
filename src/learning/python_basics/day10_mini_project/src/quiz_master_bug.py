"""
Title: Quiz Master (Buggy)
Objective: Present quiz logic errors for debugging practice.
Date: 2024-06-07
"""

questions = {
    "What keyword defines a function in Python?": "def",
    "Which data type is used to store True or False?": "bool",
    "What symbol starts a comment?": "#",
}

score = 0

for prompt, answer in questions.items():
    user_answer = input(f"{prompt} ")
    if user_answer is answer:
        print("Correct!\n")
    else:
        print(f"Oops! The correct answer was '{answer}'.\n")
        score -= 1

print(f"You scored {score} out of {len(questions)}.")
