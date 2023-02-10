#!/usr/bin/python3
'''def'''


import json


def load_from_json_file(filename):
    '''def'''
    with open(filename, "r") as file:
        return json.load(file)
