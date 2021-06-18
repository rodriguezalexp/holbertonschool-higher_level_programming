#!/usr/bin/python3
"""function to return bolean """


def divisible_by_2(my_list=[]):
    """return true or false"""
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        elif i % 2 != 0:
            new_list.append(False)
    return new_list
