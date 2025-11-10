"""
Title: Grade Classifier (Buggy)
Objective: Practice spotting mistakes in grading logic.
Date: 2024-06-07
"""

score = float(input("Enter your score (0-100): "))

if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 70:
    grade = "C"
elif score > 60:
    grade = "D"
else:
    grade = "F"

print(f"You earned a {grade}. Excellent work!")
