#!/usr/bin/python3

"""Module: Validate for UTF8"""


def validUTF8(data):
    """converts data into binary and checks starting 4 bits"""
    counter = 0

    for int in data:    
        binary = f"{int:b}"
        print(f"{int} = {binary}")
        for bit in binary[:4]:
            print(f"!{bit}!")
            if bit == '1':
                counter += 1
            print(counter)
            if len(data) > counter:
                return False
        data.remove(int)    
    return True  
