#!/usr/bin/python3
"""A module that defines a function called find_peak"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.

    Arguments:
        list_of_intergers (list): List of integers
    Return:
        integer of None
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
