#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.

    Args:
        my_list: a list can contain any type (integer, string, etc.)
        x: represents the number of elements to print

    Return:
        the real number of elements printed.
    """
    real_len = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            real_len += 1
        except IndexError:
            break
    print("", end="\n")

    return real_len
