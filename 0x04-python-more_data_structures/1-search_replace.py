#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list

    Args:
        my_list: initial listof integers
        search: element to be replaced
        replace: new element

    Return:
        new list.
    """
    return list(map(lambda nbr: nbr if nbr != search else replace, my_list))
