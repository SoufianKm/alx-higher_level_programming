#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string.

    Args:
        my_string: the string given

    Return:
        new string.
    """
    tmp_list = list(my_string)
    new_string = []
    for c in tmp_list:
        if c not in 'cC':
            new_string.append(c)
    return "".join(new_string)
