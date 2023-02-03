#!/usr/bin/python3
'''simple def'''


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except:
        return False
