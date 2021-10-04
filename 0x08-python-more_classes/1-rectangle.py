#!/usr/bin/python3
"""
Class:
    Rectangle: Defines a rectangle.
"""


class Rectangle:
    """ class Rectangle that defines a rectangle object

    Attributes:
        __width: Width of the rectangle object
        __height: Height of the rectangle object
    """
    def __init__(self, width=0, height=0):
        """Initialize method that holds the height and width of a rectangle

        Args:
             width (int): Defines width of a rectangle
             height (int): Defines height of a rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This method returns the width of a rectangle.
        """
        return (int(self.__width))

    @width.setter
    def width(self, value):
        """ Method to set the width value of the rectangle object

         Args:
            value (int): This defines the width of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This method returns the height of a rectangle.
        """
        return (int(self.__height))

    @height.setter
    def height(self, value):
        """ Method to set the height value of the rectangle object

         Args:
            value (int): This defines the height of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
