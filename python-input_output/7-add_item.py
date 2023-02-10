#!/usr/bin/python3
'''def'''


import sys
import json


def save_to_json_file(my_obj, filename):
    '''def'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    '''def'''
    with open(filename, "r") as file:
        return json.load(file)

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except:
    items = []

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, filename)
