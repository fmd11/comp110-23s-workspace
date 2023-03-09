"""Exercise 05."""

__author__ = "730320788"


def only_evens(ints: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even."""
    evens: list[int] = []
    idx: int = 0
    while idx < len(ints):
        if ints[idx]%2 ==0:
            evens.append(ints[idx])
        idx = idx +1
    return evens
    # returns all numbers divisible by 2 from a list of integers.


def sub(given_list: list[int], first_int, second_int) -> list[int]:
    """Generates a subset from a given list."""
    subset: list[int] = []
    if first_int < 0:
        first_int = 0
    if second_int > len(given_list):
            second_int = len(given_list)
    if len(given_list) == 0 or first_int >= len(given_list) or second_int <= 0:
        subset = []
    while first_int < second_int:
        subset.append(given_list[first_int])
        first_int = first_int + 1
    return subset
        # returns a list consisting of a subset of given_list.



def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Generates new list containing 2 combined lists."""
    combined: list[int] = []
    for item in list1:
        combined.append(item)
    for item2 in list2:
        combined.append(item2)
    return combined
    # return 1 list consisting of both list1 and list 2. 


li = [1, 2, 3, 4, 5]
print(sub(li, 1, 4))