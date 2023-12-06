#!/usr/bin/python3

def roman_to_int(roman_string):
    """ that converts a Roman numeral to an integer.

    Args:
        roman_string: a roman string given

    Return:
        roman numeral string converted to number
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_int = 0
    roman_numeral = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    for i in range(len(roman_string)):
        a = roman_numeral[roman_string[i]]
        if i < (len(roman_string) - 1):
            b = roman_numeral[roman_string[i + 1]]
            if a < b:
                a *= -1
        roman_int += a
    return roman_int
