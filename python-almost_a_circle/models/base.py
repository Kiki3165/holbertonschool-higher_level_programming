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
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''def json'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''def'''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, mode='w', encoding='utf-8') as file:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''def json'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''def create'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                return [cls.create(**obj) for obj in cls.from_json_string(file.read())]
        except FileNotFoundError:
            return []
