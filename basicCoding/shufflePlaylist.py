#Importing shuffle function from random module
from random import shuffle

#Creating a playlist
playlist = [
	"Blank Space -Taylor Swift",
	"Element -Kendrick Lamar",
	"Beat it - MJ",
	"Love Dose -Honey Singh",
	"Bitter Sweet Symphony -The Verve"
]

print("Before Shuffle:\n")
for eachSong in playlist:
	print(eachSong)

#Shuffling the playlist
shuffle(playlist)

print("\nAfter Shuffle:\n")
for eachSong in playlist:
	print(eachSong)
