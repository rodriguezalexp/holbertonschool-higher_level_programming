#!/usr/bin/python3
"""Funtion to multiply all values of a dict"""


def multiply_by_2(a_dictionary):
    """return values * 2"""
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
