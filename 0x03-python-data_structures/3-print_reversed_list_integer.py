#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order

    Args:
        my_list: list of integers

    Return:
        0 always.
    """
    my_list.reverse()
    for nbr in my_list:
        print("{:d}".format(nbr))
