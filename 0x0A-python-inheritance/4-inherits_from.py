#!/usr/bin/python3
""" function that returns True if the 
object is aninstance of a class"""


def inherits_from(obj, a_class):
    """if is subclass return true"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
