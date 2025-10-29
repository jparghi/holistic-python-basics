"""
Title: Grade Classifier
Objective: Translate numeric scores into descriptive letter grades.
Date: 2024-06-07
"""

score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Great job!"
elif score >= 70:
    grade = "C"
    message = "Good effort. Keep practicing."
elif score >= 60:
    grade = "D"
    message = "You passed, but review the material."
else:
    grade = "F"
    message = "Let's revisit the lessons and try again."

print(f"You earned a {grade}. {message}")
