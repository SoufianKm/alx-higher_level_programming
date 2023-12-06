#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied
    by a number without using any loops.

    Args:
        my_list: list of integers
        number: number to be multiply by

    Return:
        new list
    """
    return list(map(lambda nbr: nbr * number, my_list))
