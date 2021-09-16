#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """cpy = a_dictionary
    for i, j in a_dictionary.items():
        if j == key:
            a_dictionary[i] = value
            return a_dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
