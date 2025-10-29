"""
Title: Grocery List Manager
Objective: Demonstrate list creation, updates, and iteration.
Date: 2024-06-07
"""

groceries = []

print("Enter three grocery items:")
for _ in range(3):
    item = input("Item: ")
    groceries.append(item)

print("\nCurrent list:")
print(groceries)

remove_item = input("Which item would you like to remove? ")
if remove_item in groceries:
    groceries.remove(remove_item)
    print(f"Removed {remove_item}.")
else:
    print(f"{remove_item} was not found in the list.")

print("\nUpdated grocery list:")
for index, item in enumerate(groceries, start=1):
    print(f"{index}. {item}")
