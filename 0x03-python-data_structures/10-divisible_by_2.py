#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list.

    Args:
        my_list: list of integers

    Return:
        new list
    """
    new_list = []
    for nbr in my_list:
        if nbr % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
