#!/usr/bin/python3

"""Module: Validate for UTF8"""


def validUTF8(data):
    """Validate data for correct utf8 format"""

    valid_bool = False

    for int in data:
        if 0 < int < 255:
            valid_bool = True
        else:
            char_int = chr(int)
            if len(char_int.encode('utf-8')) <= 4:
               valid_bool = True
            else:
                return False
    return valid_bool


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

print("checker")
data = [467, 133, 108]
print(validUTF8(data))

print("checker2")
data = [235, 140]
print(validUTF8(data))