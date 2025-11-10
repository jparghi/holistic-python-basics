"""
Title: Grocery List Manager (Buggy)
Objective: Highlight common list modification mistakes.
Date: 2024-06-07
"""

groceries = ()

print("Enter three grocery items:")
for _ in range(3):
    item = input("Item: ")
    groceries.append(item)

print("\nCurrent list:")
print(groceries)

remove_item = input("Which item would you like to remove? ")
if remove_item in groceries:
    groceries.pop(remove_item)

print("\nUpdated grocery list:")
for index, item in enumerate(groceries):
    print(f"{index}. {item}")
