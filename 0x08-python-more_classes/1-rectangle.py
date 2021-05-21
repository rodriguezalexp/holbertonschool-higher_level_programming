#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """Represents a Rectangle
    Attributes:
        __Rectangle (int): size of a side of the Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle
        Args:
            width (int): size of a side of the Rectangle
                        height (int): size
        Returns: None
        """
        self.height = height
        self.width = width

    # using property decorator
    # a getter function
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    # a setter function

    @height.setter
    def height(self, value):
        """getter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
