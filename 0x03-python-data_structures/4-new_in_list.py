#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position
    without modifying the original list (like in C).

    Args:
        my_list: list of integers
        idx: position of element to be replaced
        element: the new element

    Return:
        copy of list if idx is negative or out of the range
        of length of my_listnew list, otherwise new list
    """
    copy_list = my_list.copy()
    if idx >= 0 and idx < len(copy_list):
        copy_list[idx] = element
    return copy_list
