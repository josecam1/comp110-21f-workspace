"""Finding duplicate letters in a word."""

__author__ = "730410369"

word: str = input("Enter a word: ")
check: bool = False

i: int = 0
while i < len(word):
    j: int = i + 1
    char: str = word[i]

    while j < len(word):
        if char == word[j]:
            check = True
        j += 1
        
    i += 1
print("Found duplicate: " + str(check))