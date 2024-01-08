#!/usr/bin/python3
"""
Module Matrix_divided
Divided matrix
"""


def matrix_divided(matrix, div):
    """Returns a matrix of results
    of a divided matrix
    """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")
        for i in row:
            if type(i) != int and type(i) != float:
                raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    list_row = []
    for row in matrix:
        list_row.append(len(row))
    if not all(item == list_row[0] for item in list_row):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    nbr = [[round(x / div, 2) for x in row] for row in matrix]

    return nbr
