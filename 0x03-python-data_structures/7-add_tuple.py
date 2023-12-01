#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Return:
        tuple with 2 integers
    """
    new_tuple = ()
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    a = tuple_a[0]
    b = tuple_b[0]
    c = tuple_a[1]
    d = tuple_b[1]

    return (a + b), (c + d)
