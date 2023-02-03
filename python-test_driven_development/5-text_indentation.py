#!/usr/bin/python3
'''simple def'''


def text_indentation(text):
    '''function'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = text.split()
    for i, word in enumerate(words):
        print(word, end=" ")
        if word[-1] in ".?:":
            print("\n\n")
