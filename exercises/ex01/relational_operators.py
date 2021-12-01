"""This program is supposed to run relational operators."""
__author__ = "730410369"

lhs: int = int(input("Left-hand side: "))
rhs: int = int(input("Right-hand side: "))
lessthan = (lhs) < (rhs)
isatleast = (lhs) >= (rhs)
isequalto = (lhs) == (rhs)
isnotequalto = (lhs) != (rhs)
print(str(lhs) + " < " + str(rhs) + " is " + str(lessthan))
print(str(lhs) + " >= " + str(rhs) + " is " + str(isatleast))
print(str(lhs) + " == " + str(rhs) + " is " + str(isequalto))
print(str(lhs) + " != " + str(rhs) + " is " + str(isnotequalto))