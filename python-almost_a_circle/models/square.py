#!/usr/bin/python3
'''def class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''def'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''def'''
        return self.width

    @size.setter
    def size(self, value):
        '''def'''
        self.width = value
        self.height = value

    def __str__(self):
        '''def'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''def update'''
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size,
                "x": self.__x, "y": self.__y}
