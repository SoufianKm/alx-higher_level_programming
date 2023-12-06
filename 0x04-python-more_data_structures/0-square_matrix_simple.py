#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix

    Args:
        matrix: 2 dimentional array

    Return:
        new matrix with same size as matrix
    """
    new_matrix = []
    for element in matrix:
        new_matrix.append(list(map(lambda x: x*x, element)))
    return new_matrix
