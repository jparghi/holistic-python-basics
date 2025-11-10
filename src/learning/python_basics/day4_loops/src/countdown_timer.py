"""
Title: Countdown Timer
Objective: Use a while loop to count down with a short delay.
Date: 2024-06-07
"""

import time

seconds = int(input("How many seconds should we count down? "))

while seconds > 0:
    print(f"{seconds}...")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
