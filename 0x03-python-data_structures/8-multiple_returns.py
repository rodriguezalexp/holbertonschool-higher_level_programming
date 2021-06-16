#!/usr/bin/python3
"""function with two returns"""


def multiple_returns(sentence):
    """return lenght and fir char of a string"""
    if not sentence:
        return len(sentence), 0
    else:
        return len(sentence), sentence[0]
