#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list like in C.

    Args:
        my_list: list of integers
        idx: index of element

    Return:
        element at index, otherwise None
    """
    if idx >= 0 and idx < len(my_list):
        return my_list[idx]
