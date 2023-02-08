#!/usr/bin/python3
'''simple class'''


class BaseGeometry:
    '''simple def'''
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        '''simple def'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
