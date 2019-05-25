#!/usr/bin/python3
"""
This Module contains afunction to prin a full name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print the full name.
    @first_name: first name of user.
    @last_name: is a last name user.
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
