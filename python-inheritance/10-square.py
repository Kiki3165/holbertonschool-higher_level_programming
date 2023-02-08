#!/usr/bin/python3
'''simple def'''


Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    '''def'''
    def __init__(self, size):
        '''def'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return'''
        return self.__size ** 2

    def __str__(self):
        '''return'''
        return "[Square] {}/{}".format(self.__size, self.__size)
