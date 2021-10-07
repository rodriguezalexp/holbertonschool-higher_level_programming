#!/usr/bin/python3
"""Create mul module
>>> mul(3, 6)
18
"""

def mul(a, b):
    """Test mul module
    >>> mul(1, 3) #doctest: +REPORT_NDIFF
    3#
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
