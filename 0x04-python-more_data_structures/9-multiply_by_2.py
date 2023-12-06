#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: dictonary given

    Return:
        new dictionary
    """
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return new_dictionary
