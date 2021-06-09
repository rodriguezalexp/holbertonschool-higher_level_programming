#!/usr/bin/python3
"""square class definition"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
