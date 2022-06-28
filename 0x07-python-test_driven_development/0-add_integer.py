#!/usr/bin/python3

""" adder function with test case"""

def add_integer(a, b=98):
    """adder function with two param a and b"""

    if type(a) not in [int,float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int,float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

