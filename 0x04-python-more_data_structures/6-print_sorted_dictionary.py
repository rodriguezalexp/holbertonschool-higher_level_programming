#!/usr/bin/python3
"""Function print sorted dictionary"""


def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(i, a_dictionary[i]))
