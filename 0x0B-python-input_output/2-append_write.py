#!/usr/bin/python3
"""write to the end of a txt file"""


def append_write(filename="", text=""):
    """return the len of txt file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
