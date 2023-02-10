#!/usr/bin/python3
'''def'''


def write_file(filename="", text=""):
    '''def'''
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
