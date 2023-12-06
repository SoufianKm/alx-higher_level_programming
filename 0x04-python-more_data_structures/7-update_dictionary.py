#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dictionary given
        key: argument
        value: value of argument

    Return:
        new dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
