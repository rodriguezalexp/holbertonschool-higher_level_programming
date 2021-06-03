#!/usr/bin/python3
"""function that returns an object represented by
a Json string"""
import json


def save_to_json_file(my_obj, filename):
    """return object"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
