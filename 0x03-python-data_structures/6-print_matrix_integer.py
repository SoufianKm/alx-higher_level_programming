#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers.

    Args:
        matrix: list of 3 lists of length 3

    Retrun:
        0 always.
    """
    length = 0
    for col in matrix:
        for nbr in col:
            length += 1
            if length < len(col):
                print(nbr, end=" ")
            else:
                print(nbr, end="")
        print("\n", end="")
        length = 0
