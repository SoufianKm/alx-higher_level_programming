#!/usr/bin/python3

def common_elements(set_1, set_2):
    """returns a set of common elements in two sets

    Args:
        set_1: first list
        set_2: seconde list

    Return:
        a set of common elements in two sets
    """
    new_set = []
    for element in set_1:
        if element in set_2:
            new_set.append(element)

    return new_set
