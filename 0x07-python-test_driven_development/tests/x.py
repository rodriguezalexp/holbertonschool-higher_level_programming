#!/usr/bin/python3
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,
add two integers

>>> sum(5, 3)
8
"""

def sum(a, b):
    """ Testing add function
    >>> sum('a', 3)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    >>> sum(-1 + -17)

    """

    if type(a) and type(b) is not int:
        raise TypeError("only integers")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()