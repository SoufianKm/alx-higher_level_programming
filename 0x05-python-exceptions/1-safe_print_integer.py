#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value: can contain any type (integer, string, etc.)

    Return:
        True if value has been correctly printed, Otherwise False.
    """
    res = False
    try:
        int_val = int(value)
        print("{:d}".format(int_val), end="\n")
        res = True
    except ValueError:
        res = False
    return res
