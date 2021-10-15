#!/usr/bin/python3
"""""Rectangle Class Definition"""


class Rectangle:
    """Representation of Rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private intance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @width.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >0")
        else:
            self.__height = value

    def area(self):
        """The area representation of a rectangle"""
        self.__width * self.__height

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for i in range(self.__width):
                for j in range(self.__height):
                    str += '#'
                str += '/n'
            return str[:-1]

    def __del__(self):
        """"""
        del self
        print("Bye Rectangle...")
