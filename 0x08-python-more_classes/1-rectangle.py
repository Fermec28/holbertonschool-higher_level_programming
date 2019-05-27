#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width


    @property
    def height(self):
        return self.height


    @width.setter
    def width(self, value):
        self.__width = value


    @height.setter
    def height(self, value):
        self.__height = value
