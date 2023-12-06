#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value.

    Args:
        a_dictionary: dictionary given

    Return:
        new dictionary
    """
    the_best = None
    if a_dictionary:
        the_best = list(a_dictionary)[0]
        for key in a_dictionary:
            biggest_int = a_dictionary[the_best]
            if a_dictionary[key] > biggest_int:
                biggest_int = a_dictionary[key]
                the_best = key

    return the_best
