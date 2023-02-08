#!/usr/bin/python3
'''simple class'''


class Rectangle(BaseGeometry):
    '''simple def'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
