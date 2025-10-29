"""
Title: Contact Book (Buggy)
Objective: Emphasize dictionary key errors and update issues.
Date: 2024-06-07
"""

contacts = {
    "Avery": "avery@example.com",
    "Jordan": "jordan@example.com",
}

print("Current contacts:")
for name, email in contacts:
    print(f"- {name}: {email}")

new_name = input("Enter a new contact name: ")
new_email = input("Enter the contact's email: ")
contacts.update(new_name, new_email)

print("\nUpdated contacts:")
for name, email in contacts.items():
    print(f"- {name}: {email}")
