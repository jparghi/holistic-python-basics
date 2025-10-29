"""
Title: Playlist Editor (Buggy)
Objective: Provide list slicing issues for debugging practice.
Date: 2024-06-07
"""

playlist = (
    "Sunrise Groove",
    "Ocean Waves",
    "City Lights",
    "Mountain Echo",
)

print("Original playlist:")
print(playlist)

first_song = playlist.pop(0)
playlist.insert(-1, first_song)

print("\nAfter moving the first song to the end:")
print(playlist)

playlist[1:3] = "Desert Drive"

print("\nAfter updating the middle tracks:")
print(playlist)
