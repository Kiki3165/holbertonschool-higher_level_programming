#!/usr/bin/python3
'''def'''


class Student:
    '''class'''
    def __init__(self, first_name, last_name, age):
        '''def'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''def'''
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {
                attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        '''def'''
        for key in json:
            setattr(self, key, json[key])
