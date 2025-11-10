"""
Title: Weather Advisor
Objective: Provide clothing suggestions based on weather conditions.
Date: 2024-06-07
"""

temperature = float(input("Enter the temperature in Celsius: "))
condition = input("Is it rainy, sunny, or windy? ").strip().lower()

if temperature < 5:
    outfit = "a heavy coat, gloves, and a hat"
elif temperature < 15:
    outfit = "a jacket and a warm scarf"
elif temperature < 25:
    outfit = "a light sweater or long sleeves"
else:
    outfit = "short sleeves and breathable fabrics"

if condition == "rainy":
    accessory = "Remember your umbrella!"
elif condition == "windy":
    accessory = "A windbreaker will help."
else:
    accessory = "Enjoy the nice weather!"

print(f"Wear {outfit}. {accessory}")
