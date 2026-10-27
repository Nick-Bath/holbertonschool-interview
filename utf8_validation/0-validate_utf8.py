#!/usr/bin/python3

"""Module: Validate for UTF8"""


def validUTF8(data):
    """converts data into binary and checks starting 4 bits"""
    counter = 0

    for int in data:    
        binary = f"{int:b}"
        for bit in binary[:4]:
            if bit == '1':
                counter += 1
            if len(data) > counter:
                return False
        data.remove(int)    
    return True  
