#!/usr/bin/python3
"""My list class """


class MyList(list):
    """subclass of mylist"""

    def __init__(self):
        """init the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
