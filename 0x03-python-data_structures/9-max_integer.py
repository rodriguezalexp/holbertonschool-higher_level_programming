#!/usr/bin/python3
"""Funtion to compare the max value of a list"""


def max_integer(my_list=[]):
    """find the max value with a for func"""
    max_value = None

    for i in my_list:
        if (max_value is None or i > max_value):
            max_value = i
    return max_value
