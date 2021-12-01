"""Drawing forests in a loop."""

__author__ = "730410369"

# The string constant for the pine tree emoji

TREE: str = '\U0001F332'

depth: int = int(input("What is your depth? "))

i: int = 0 
spruce: str = ""

while i < depth:
    if depth < 1:
        print("Depth: " + str(depth))
    else:
        spruce = spruce + TREE
        print(spruce)
    i += 1
if depth < 1:
    print("Depth: " + str(depth))