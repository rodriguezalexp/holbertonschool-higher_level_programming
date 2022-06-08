#!/usr/bin/python3
"""Class to define a square"""


class Square:

    """representation class of of a square
    """
    def __init__(self, size=0):
        """Constructor of class"""
        self.size = size

    @property
    def size(self):
        """ Getter decorator to return the size of a square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter to set the size value"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def my_print(self):
        """Method to print square representation"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
