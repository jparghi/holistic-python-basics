"""
Title: Countdown Timer (Buggy)
Objective: Provide a faulty countdown for debugging practice.
Date: 2024-06-07
"""

import time

seconds = int(input("How many seconds should we count down? "))

while seconds >= 0:
    print(f"{seconds}...")
    time.sleep(1)

print("Time's up!")
