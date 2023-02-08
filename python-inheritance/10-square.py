#!/usr/bin/python3
'''simple def'''


Rectangle = __import__("8-rectangle.py").Rectangle


class Square(Rectangle):
    '''def'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
