#!/usr/bin/python3
""" Funtion to return json representation"""
import json


def from_json_string(my_str):
    """return json obj"""

    return json.loads(my_str)
