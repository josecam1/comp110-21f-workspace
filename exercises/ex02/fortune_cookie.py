"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730410369"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
positive_vibe: int = randint(1, 4)
if positive_vibe == 1:
    print("The bag will come your way.")
else:
    if positive_vibe == 2:
        print("You will pass your exercise!")
    else:
        if positive_vibe == 3:
            print("An amazing friend is waiting nearby.")
        else: 
            print("Your finance meeting will go the way you want it to.")
print("Now, go spread positive vibes!")