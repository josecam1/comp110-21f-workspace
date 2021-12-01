"""List utility functions part 2."""

__author__ = "730410369"


def only_evens(group: list[int]) -> list[int]:
    """Find values are only even."""
    even: int
    i: int = 0
    while i < len(group):
        even += group[i]
        i += 1
    return even
