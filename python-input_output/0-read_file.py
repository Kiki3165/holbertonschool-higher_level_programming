#!/usr/bin/python3
'''def'''


def read_file(filename=""):
    '''def'''
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
