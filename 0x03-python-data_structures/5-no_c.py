#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string.

    Args:
        my_string: the string given

    Return:
        new string.
    """
    if my_string:
        tmp_list = list(my_string)
        for c in tmp_list:
            if c in 'cC':
                tmp_list.remove(c)
        return "".join(tmp_list)
    return my_string
