#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda element: list(map(lambda nbr: nbr * nbr, element)), matrix))
