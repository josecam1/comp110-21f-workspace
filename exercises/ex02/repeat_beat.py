"""Repeating a beat in a loop."""

__author__ = "730410369"


# Begin your solution here...

counter: int = 0
print(counter)
counter = counter + 1

sound: str = str(input("What beat do you want to repeat? ")) 

bars: int = int(input("How many times do you want to repeat it? "))

beat = ""
if bars <= 0:
    print("No beat...")
else:
    while counter <= bars:
        if counter < bars:
            beat = beat + sound + " "
            counter = counter + 1
        else: 
            beat = beat + sound
            counter = counter + 1

print(beat)
