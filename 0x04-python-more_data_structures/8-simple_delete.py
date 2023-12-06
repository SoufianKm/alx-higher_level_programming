#!/usr/bin/pyhton3

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.

    Args:
        a_dictionary: dictionary given
        key: string argument

    Return:
        new dictionary
    """
    if key in a_dictionary:
        if a_dictionary[key] is not None:
            new_dictionary = {}
            for a_key in a_dictionary:
                if key != a_key: 
                    new_dictionary[a_key] = a_dictionary[a_key]
            return new_dictionary

    return a_dictionary
