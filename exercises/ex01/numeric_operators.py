"""This program is supposed to run numeric operators"""
__author__ = "730410369"

lhs: int = int(input("Left-hand side: "))
rhs: int = int(input("Right-hand side: "))
exp = (lhs) ** (rhs)
div = (lhs) / (rhs)
intdiv = (lhs) // (rhs)
modulo = (lhs) % (rhs)
print(str(lhs) + " ** " + str(rhs) + " is " + str(exp))
print(str(lhs) + " / " + str(rhs) + " is " + str(div))
print(str(lhs) + " // " + str(rhs) + " is " + str(intdiv))
print(str(lhs) + " % " + str(rhs) + " is " + str(modulo))