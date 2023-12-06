#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value.

    Args:
        a_dictionary: dictionary given

    Return:
        new dictionary
    """
    if a_dictionary:
        return list(sorted(a_dictionary))[-1]

    return None
