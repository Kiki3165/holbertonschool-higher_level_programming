#!/usr/bin/python3
'''def class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''def'''
        super().__init__(id)
        self.width = size
        self.height = size
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        '''def str'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def display(self):
        '''def display'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def area(self):
        '''def area'''
        return self.__width * self.__height
