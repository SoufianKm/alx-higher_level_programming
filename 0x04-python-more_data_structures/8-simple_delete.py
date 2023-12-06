#!/usr/bin/pyhton3

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.

    Args:
        a_dictionary: dictionary given
        key: string argument

    Return:
        new dictionary
    """
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]

    return a_dictionary
