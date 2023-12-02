#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order

    Args:
        my_list: list of integers

    Return:
        0 always.
    """
    tmp_list = my_list.copy()
    tmp_list.reverse()
    for nbr in tmp_list:
        print("{:d}".format(nbr))
