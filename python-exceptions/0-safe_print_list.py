#!/usr/bin/python3
'''simple def'''


def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elements_printed += 1
        print()
    except:
        print()
    return elements_printed
