#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string
    and its first character.

    Args:
        sentence: the string given

    Return:
        tuple with the length of a string, if sentence
        is empty return 0 on length and None as first character
    """
    if sentence:
        return len(sentence), sentence[0]
    else:
        return 0, "None"
