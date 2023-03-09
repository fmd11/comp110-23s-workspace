"""EX04  'list' Utility Functions."""


__author__ = "730320788"


def max(input: list[int]) -> int:
    """Returns the largest int in the List."""
    largest_int: int = input[0]
    idx_2: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")    # shows error for empty list.
    while idx_2 < len(input):
        if input[idx_2] > largest_int:
            largest_int = input[idx_2]
        idx_2 = idx_2 + 1
    return largest_int    # returns the highest value number in the list.


def all(int_list: list[int], given_int: int) -> bool:
    """Indicates if ints in list are the same as the given int.""" 
    idx: int = 0 
    if len(int_list) == 0:
        return False   # list is empty.
    while idx < len(int_list):
        if int_list[idx] != given_int:
            return False   # not all numbers match the indicated number.
        else:
            idx = idx + 1
    return True   # all numbers match the indicated number.


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Indicates if every element at every index is = in 2 lists."""
    idx_3: int = 0 
    if len(list1) != len(list2):
        return False   # lists are not equal.
    while idx_3 < len(list1):
        if list1[idx_3] != list2[idx_3]:
            return False   # lists are not equal.
        idx_3 = idx_3 + 1
    return True   # lists are equal.