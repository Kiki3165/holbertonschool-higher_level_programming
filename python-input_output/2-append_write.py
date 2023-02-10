#!/usr/bin/python3
'''def'''


def append_write(filename="", text=""):
    '''def'''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
