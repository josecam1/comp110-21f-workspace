"""List utility functions."""

__author__ = "730410369"
# TODO: Implement your functions here.


# def all(numlist: list[int], number: int):
#     i = 0
#     # j = 0
#     while i < len(numlist) - 1:
#         if numlist[i] != number:
#             return False
#         else:
#             i = i + 1
#     return i == len(numlist)


# print(all([1, 1, 1], 1))


# def all(numlist: list[int], number: int) -> bool:

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks to see if the lists have the same values."""
    i = 0
    j = 0
    if len(list_one) == len(list_two):
        if list_one[i] == list_two[i]: 
            while i < len(list_one) and j < len(list_two):
                print(list_one)
                print(list_two)
                i = i + 1
                j = j + 1
        else:
            return None
    else:
        return None

is_equal([1, 2, 3], [1, 2, 3])
print(is_equal())