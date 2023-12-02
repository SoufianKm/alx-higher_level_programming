#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list.

    Args:
        mu_list: list of integers

    Return:
        the max integer
    """
    if my_list:
        max_int = my_list[0]
        for nbr in my_list:
            if nbr > max_int:
                max_int = nbr
    else:
        max_int = "None"

    return max_int
