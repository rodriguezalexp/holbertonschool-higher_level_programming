#!/usr/bin/python3
"""Class to define a rectangle"""


class Rectangle:
    """Defining a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class contructor
        parameters:
        width: paramereter to define a width for a Rectangle
        Height: parameter to define a height for a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter of with method"""
        return self.__width

    @width.setter
    def width(self, value):
        """settter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to return area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """string representation of Rectangle based on a symbol"""
        new_str = ""
        if self.__width == 0 or self.height == 0:
            return new_str
        new_str += "\n".join(str(Rectangle.print_symbol) * self.__width
                             for j in range(self.__height))
        print(type(new_str))
        return new_str

    def __repr__(self):
        """Oficial representacion of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """del method to delete a object instance of class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """staticmethod to compare the biggest Rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(1, 8)

try:
    print(my_rectangle_2 == Rectangle.bigger_or_equal(my_rectangle_1, "Rect"))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))