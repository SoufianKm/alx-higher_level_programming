#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific
    position (like in C).

    Args:
        my_list: list of integer
        idx: position of element to be replaced
        element: new element

    Return:
        if idx is negative or out of range of my_list
        it returns the original list
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
