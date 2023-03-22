"""CQ 04 - Dict Function Writing."""

__author__ = "730320788"

def zip(int_list: list[int], str_list: list[str]) -> dict[str, int]:
    """produces a dictionary of keys and values"""
    if len(int_list) == 0 or len(str_list) == 0 or len(str_list) != len(int_list):
        return dict()
    dictionary = {}
    for idx in range(len(int_list)):
        dictionary[int_list[idx]] = str_list[idx]
    return dictionary