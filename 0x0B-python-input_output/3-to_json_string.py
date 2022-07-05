#!/usr/bin/python3
""" Module that contains a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object
    Args:
        my_obj: object
    """
    return json.dumps(my_obj)
