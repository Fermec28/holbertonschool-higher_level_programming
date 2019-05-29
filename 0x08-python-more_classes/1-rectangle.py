#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Constructor
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter of width
        """
        return self.width

    @property
    def height(self):
        """
        getter of height
        """
        return self.height

    @width.setter
    def width(self, value):
        """
        setter of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
