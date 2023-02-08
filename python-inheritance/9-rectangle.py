#!/usr/bin/python3
'''simple def'''



BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''def'''
    def __init__(self, width, height):
        '''docu'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''return'''
        return self.__width * self.__height

    def __str__(self):
        '''return'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
