#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value: can contain any type (integer, string, etc.)

    Return:
        True if value has been correctly printed, Otherwise False.
    """
    try:
        print("{:d}".format(value), end="\n")
        return True
    except TypeError:
        return False
