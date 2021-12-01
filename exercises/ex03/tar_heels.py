"""An exercise in remainders and boolean logic."""

__author__ = "730410369"


# Begin your solution here...

integer = int(input(("Enter a number: ")))

if integer % 2 == 0 and integer % 7 == 0:
    print("TAR HEELS")
elif integer % 2 == 0:
    print("TAR")
elif integer % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")
