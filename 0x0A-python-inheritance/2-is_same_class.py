#!/usr/bin/python3
"""this function detect if the object
is an instance of specific class"""


def is_same_class(obj, a_class):
    """find incidences """
    if type(obj) == a_class:
        return True
    else:
        return False
