"""
Title: Set Operations Explorer (Buggy)
Objective: Provide faulty set operations for debugging practice.
Date: 2024-06-07
"""

student_hobbies = ["painting", "cycling", "gaming"]
friend_hobbies = ["gaming", "hiking", "reading"]

print(f"Shared hobbies: {student_hobbies.intersection(friend_hobbies)}")
print(f"All hobbies: {student_hobbies.union(friend_hobbies)}")
print(f"Unique to student: {student_hobbies.difference(friend_hobbies)}")
print(f"Unique to friend: {friend_hobbies.difference(student_hobbies)}")
