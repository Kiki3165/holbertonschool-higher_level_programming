#!/usr/bin/python3
'''def class'''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''def'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        '''def area'''
        return self.__width * self.__height

    def display(self):
        '''def display'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''def str'''
        return f"[Rectangle] ({id=}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''def update'''
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        '''def'''
        return self.__width

    @width.setter
    def width(self, value):
        '''def'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''def'''
        return self.__height

    @height.setter
    def height(self, value):
        '''def'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''def'''
        return self.__x

    @x.setter
    def x(self, value):
        '''def'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''def'''
        return self.__y

    @y.setter
    def y(self, value):
        '''def'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        '''def dict'''
        return {key[12:]: value for key, value in self.__dict__.items() if key.startswith('_Rectangle')}
