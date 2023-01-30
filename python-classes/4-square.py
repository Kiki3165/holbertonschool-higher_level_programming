#!/usr/bin/python3
'''def class'''


class Square:
    '''simple def'''
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    
    '''simple def'''
    def area(self):
        return self.__size ** 2

    '''simple def'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
