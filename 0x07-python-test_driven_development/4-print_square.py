#!/usr/bin/python3
"""
Module to print_square
"""


def print_square(size):
    """
    Function to print a square size x size.
    @size (int, float > 0): size of the square.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print("{}".format("#"*int(size)))
