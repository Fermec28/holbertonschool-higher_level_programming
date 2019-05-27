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
        return self.__width

    @property
    def height(self):
        """
        getter of height
        """
        return self.__height

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate area of Rectangle
        """
        return self.__height * self.width

    def perimeter(self):
        """
        calculate perimetter of Rectangle
        """
        return 2 * self.__height + 2 * self.width
