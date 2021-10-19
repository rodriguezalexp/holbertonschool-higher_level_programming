#!/usr/bin/python3
"""defines a class Base"""
import json


class Base:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
