#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for key in sorted(a_dictionary):
        a_dictionary[key] = value
