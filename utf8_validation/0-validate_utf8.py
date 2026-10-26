#!/usr/bin/python3

"""Module: Validate for UTF8"""


def validUTF8(data):
    """Validate data for correct utf8 format"""

    valid_bool = False

    for int in data:
        if int < 128:
            valid_bool = True
        else:
            valid_bool = False
    return valid_bool
