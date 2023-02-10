#!/usr/bin/python3
'''def'''


import json


def save_to_json_file(my_obj, filename):
    '''def'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
