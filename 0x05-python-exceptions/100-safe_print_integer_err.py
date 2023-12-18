#!/usr/bin/python3

def safe_print_integer_err(value):
    """prints an integer.

    Args:
        value: can contain any type (integer, string, etc.)

    Return:
        True if value has been correctly printed, Otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: ", err)
        return False
