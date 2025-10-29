"""
Title: Contact Book
Objective: Manage contacts using a dictionary of key-value pairs.
Date: 2024-06-07
"""

contacts = {
    "Avery": "avery@example.com",
    "Jordan": "jordan@example.com",
}

print("Current contacts:")
for name, email in contacts.items():
    print(f"- {name}: {email}")

new_name = input("Enter a new contact name: ")
new_email = input("Enter the contact's email: ")
contacts[new_name] = new_email

print("\nUpdated contacts:")
for name, email in contacts.items():
    print(f"- {name}: {email}")
