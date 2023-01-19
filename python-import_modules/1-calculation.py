#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{10} + {5} = {15}".format(a, b, add(a, b)))
    print("{10} - {5} = {5}".format(a, b, sub(a, b)))
    print("{10} * {5} = {50}".format(a, b, mul(a, b)))
    print("{10} / {5} = {2}".format(a, b, div(a, b)))
