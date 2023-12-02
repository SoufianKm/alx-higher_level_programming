#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers.

    Args:
        matrix: list of 3 lists of length 3

    Retrun:
        0 always.
    """
    for col in matrix:
        length = 1
        for nbr in col:
            if length < len(col):
                print("{:d}".format(nbr), end=" ")
            else:
                print("{:d}".format(nbr), end="")
            length += 1
        print()
