#!/usr/bin/python3
'''def class'''


import json


class Base:
    '''class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(json_string):
        '''def json'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''def'''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, mode='w', encoding='utf-8') as file:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_dict))
