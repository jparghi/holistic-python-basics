"""
Title: Playlist Editor
Objective: Practice slicing and reordering items in a list.
Date: 2024-06-07
"""

playlist = [
    "Sunrise Groove",
    "Ocean Waves",
    "City Lights",
    "Mountain Echo",
]

print("Original playlist:")
print(playlist)

first_song = playlist.pop(0)
playlist.append(first_song)

print("\nAfter moving the first song to the end:")
print(playlist)

playlist[1:3] = ["Desert Drive", "Forest Whisper"]

print("\nAfter updating the middle tracks:")
print(playlist)
