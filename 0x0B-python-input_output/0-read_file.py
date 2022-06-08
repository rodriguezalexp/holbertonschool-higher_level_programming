#!/usr/bin/python3
"""function that reads and print a text file"""


def read_file(filename=""):
    """print the file text"""
    with open(filename, encoding="utf-8") as fichero:
        print(fichero.read(), end="")
