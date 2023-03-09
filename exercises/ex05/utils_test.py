"""Exercise 05 Test Part."""

__author__ = "730320788"


from exercises.ex05.utils import only_evens, concat, sub

def test_1_only_evens() -> None:
    """Tests if the function will return a single integer if only one even interger is present."""
    int_list: list[int] = [1, 2, 3, 5]
    assert only_evens(int_list)


def test_2_only_evens() -> None:
    """Tests if the list is made only up of all the even intergers from the list."""
    int_list: list[int] = [6, 7, 8, 9, 10]
    assert only_evens(int_list)


def test_3_only_evens() -> None:
    """Tests if the function returns full list if list contains only even integers."""
    int_list: list[int] = [12, 22, 32, 42, 52]
    assert only_evens(int_list)


def test_1_concat() -> None:
    """Tests if the function combines lists when one list is empty."""
    int_1list: list[int] = [11, 12, 13, 14]
    int_2list: list[int ]= []
    assert concat(int_1list, int_2list)


def test_2_concat() -> None:
    """Tests if the function combines lists with different lengthed integers."""
    int_1list: list[int] = [1, 2, 3, 4]
    int_2list: list[int ]= [2100, 2200, 2300, 2400]
    assert concat(int_1list, int_2list)


def test_3_concat() -> None:
    """Tests if the function combines lists that are different lengths."""
    int_1list: list[int] = [1, 2, 3, 4]
    int_2list: list[int ]= [5, 6, 7, 8, 9, 10, 11]
    assert concat(int_1list, int_2list)


def test_1_sub() -> None:
    """Tests if function will create the subset list if the first interger given is a negative."""
    int_1list: list[int] = [1, 2, 3, 4]
    first_int: int = -1
    second_int: int = 2
    assert sub(int_1list, first_int, second_int)


def test_2_sub() -> None:
    """Tests if function will create the subset list if the second interger given is larger than the length of the list."""
    int_1list: list[int] = [1, 2, 3, 4, 5]
    first_int: int = 1
    second_int: int = 12
    assert sub(int_1list, first_int, second_int)


def test_3_sub() -> None:
    """Tests if function will create the subset list if the first integer is 0."""
    int_1list: list[int] = [0, 1, 2, 3, 4, 5, 6]
    first_int: int = 0
    second_int: int = 4
    assert sub(int_1list, first_int, second_int)