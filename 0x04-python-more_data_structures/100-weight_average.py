#!/usr/bin/python3

def weight_average(my_list=[]):
    """return the weighted average of all integers tuple

    Args:
        my_list: list on integers

    Return:
        weighted average of all integers tuple, otherwise 0
    """
    result = 0
    if my_list:
        total_numerator = 0
        total_denominator = 0
        numerator = list(map(lambda nbr: (nbr[0] * nbr[1]), my_list))
        denominator = list(map(lambda nbr: nbr[1], my_list))
        for element in numerator:
            total_numerator += element

        for element in denominator:
            total_denominator += element

        result = (float)(total_numerator / total_denominator)

    return result
