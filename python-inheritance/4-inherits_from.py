#!/usr/bin/python3
'''simple def'''


def inherits_from(obj, a_class):
    '''return'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
