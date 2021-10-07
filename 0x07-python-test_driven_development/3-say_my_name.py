#!/usr/bin/python3
"""
This is the "3-say_my-name" module.
The 3-say_my_name  module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """ Prints "My name is" followed by the first name and optional last name

    Args:
        first_name (str): string thah contain a name
        last_name (str, optional): optional argument for a last name.

    Raises:
        TypeError: first_name must be a string"
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
