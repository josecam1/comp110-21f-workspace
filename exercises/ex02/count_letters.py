"""Counting letters in a string."""

__author__ = "730410369"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i = int = 0
counter = 0
while i < len(word):
    if word[i] == letter:
        counter = counter + 1
        i = i + 1
    else: 
        i = i + 1


print("Count: " + str(counter))