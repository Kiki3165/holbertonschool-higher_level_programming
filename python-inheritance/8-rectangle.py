#!/usr/bin/python3
'''simple class'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''simple def'''

    def __init__(self, width, height):
        '''docu'''
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
