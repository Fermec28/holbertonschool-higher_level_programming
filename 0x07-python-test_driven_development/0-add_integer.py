#!/usr/bin/python3
"""
This module contains a function to add two numbers
"""


def add_integer(a, b=98):
    """
    Add two numbers
    Parameters:
    @a: Number1
    @b: Number2
    Return: Sum of two numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
