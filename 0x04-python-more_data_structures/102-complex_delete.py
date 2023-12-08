#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary

    Args:
        a_dictionary: dictionary given
        value: value element in the dictionary to be deleted

    Return:
        0 always
    """
    if a_dictionary.values():
        for key, val in sorted(a_dictionary.items()):
            if value in val:
                del a_dictionary[key]

    return a_dictionary
