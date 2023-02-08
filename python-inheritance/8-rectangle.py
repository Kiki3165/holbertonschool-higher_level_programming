#!/usr/bin/python3
'''simple class'''



class Rectangle(BaseGeometry):
    '''simple def'''
    def __init__(self, width, height):
        '''docu'''
        self.integer_validator("width", width)
        '''dede'''
        self._width = width
        '''deffr'''
        self.integer_validator("height", height)
        '''frfed'''
        self._height = height
