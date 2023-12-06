#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)

    Args:
        my_list: list of integers

    Return:
        sum of unique integers
    """
    tmp_list = []
    result = 0
    for nbr in my_list:
        if nbr not in tmp_list:
            tmp_list.append(nbr)
            result += nbr

    return result
