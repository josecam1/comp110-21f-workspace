"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def only_evens_empty() -> None:
    group: list[int] = []
    assert sum(group) == 0


def only_evens_single_item() -> None:
    group: list[int] = [110]
    assert sum(group) == 110


def only_evens_many_items() -> None:
    group: list[int] = [1, 2, 3]
    assert sum(group) == 6


# def only_evens_many_items_again() -> None:
#     assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0