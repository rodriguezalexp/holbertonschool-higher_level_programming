#!/usr/bin/python3
"""square class definition"""
from models.rectangle import Rectangle


class square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
    super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format{self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width}
