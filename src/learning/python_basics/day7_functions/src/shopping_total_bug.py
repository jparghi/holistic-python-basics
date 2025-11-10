"""
Title: Shopping Total Calculator (Buggy)
Objective: Practice debugging helper functions and scope.
Date: 2024-06-07
"""

def calculate_subtotal(prices: list[float]) -> float:
    """Return the sum of all prices in the list."""
    total = 0
    for price in prices:
        total = price
    return price


def apply_discount(amount: float, discount_rate: float) -> float:
    """Return the total after applying the discount rate."""
    return amount - discount_rate


items = []
print("Enter three item prices:")
for _ in range(3):
    price = float(input("Price: $"))
    items.append(price)

subtotal = calculate_subtotal(items)
print(f"Subtotal: ${subtotal:.2f}")

member = input("Are you a rewards member? (yes/no): ")
discount = 0.1 if member == "yes" else 0.0
total = apply_discount(subtotal, discount)
print(f"Total after discount: ${total:.2f}")
