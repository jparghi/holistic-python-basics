"""
Title: Set Operations Explorer
Objective: Demonstrate set union, intersection, and difference.
Date: 2024-06-07
"""

student_hobbies = {"painting", "cycling", "gaming"}
friend_hobbies = {"gaming", "hiking", "reading"}

print(f"Shared hobbies: {student_hobbies & friend_hobbies}")
print(f"All hobbies: {student_hobbies | friend_hobbies}")
print(f"Unique to student: {student_hobbies - friend_hobbies}")
print(f"Unique to friend: {friend_hobbies - student_hobbies}")
