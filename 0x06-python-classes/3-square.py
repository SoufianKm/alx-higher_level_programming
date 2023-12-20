#!/usr/bin/python3
""" this module defines a empty class square """


class Square:
    """ class defines a square """
    def __init__(self, size=0):
        """ Initialize class """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
