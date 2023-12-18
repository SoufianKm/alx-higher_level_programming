#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely.

    Args:
        args: list of argument

    Return:
        the result of the function. Otherwise, returns None
    """
    try:
        res = fct(*args)
    except BaseException as e:
        res = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return res
