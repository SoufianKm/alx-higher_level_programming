#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list.

    Args:
        my_list: list of integers
        idx: index of element to be deleted

    Return:
        new list, otherwise original list
    """
    if idx >= 0 and idx < len(my_list):
        for nbr in my_list:
            if my_list.index(nbr) == idx:
                my_list.remove(nbr)
    return my_list
