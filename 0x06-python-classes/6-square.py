#!/usr/bin/python3
""" this module defines a empty class square """


class Square:
    """ class defines a square

    Attributes:
            size: integer size of square
            postion: a tuple of 2 positive integers
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize class

        Args:
            size: integer size
            postion: a tuple of 2 positive integers

        Return:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter of size

        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size

        Args:
            value: integer size

        Raises
            TypeError: if size is not int
            ValueError: size less than 0

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        get postion attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of position

        Args:
            value: position of the square in 2D space

        Return:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        get area

        Return:
            area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square

        Return:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
