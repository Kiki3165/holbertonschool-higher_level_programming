#!/usr/bin/python3
'''simple def'''


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is None:
        return a_dictionary
    else:
        a_dictionary.pop(key)
        return a_dictionary
