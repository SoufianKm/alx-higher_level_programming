#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """x retriever.

        Returns:
            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x.

        Args:
            value (int): x.
        """
        self.__x = value

    @property
    def y(self):
        """y retriever.

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y.

        Args:
            value (int): y.
        """
        self.__y = value
