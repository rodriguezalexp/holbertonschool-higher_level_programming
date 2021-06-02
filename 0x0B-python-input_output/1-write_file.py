#!/usr/bin/python3
"""function that write a text file"""


def write_file(filename="", text=""):
    """return the len of txt file"""
    with open(filename, 'W', encoding="utf-8") as f:
        return f.write(text)
