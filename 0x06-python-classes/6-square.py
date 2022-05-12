#!/usr/bin/python3
"""class to defina a square"""


class Square:
    """Definining a class square"""
    
    def __init__(self, size=0, position=(0, 0)):
        """class constructor to instance a size value"""
        self.size = size
        self.position = position
        
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """Getter property of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter method of size"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    def my_print(self):
        """print square representation with # character """
        if self.size == 0:
            print()
        if self.__position[1]:
            print()
        for i in range(self.__size):
            print("".join([" " for i in range(self.__position[0])]), end="")
            print("".join(["#" for j in range(self.__size)]))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")