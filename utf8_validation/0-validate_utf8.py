#!/usr/bin/python3

"""Module: Validate for UTF8"""


def validUTF8(data):
    """Validate data for correct utf8 format"""

    valid_bool = False

    for int in data:
        if 0 < int < 255:
            valid_bool = True
        else:
            binary = f"{int:b}"
            return False
    return valid_bool
