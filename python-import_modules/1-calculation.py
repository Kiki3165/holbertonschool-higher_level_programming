#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    result1 = add(a, b)
    result2 = sub(a, b)
    result3 = mul(a, b)
    result4 = div(a, b)
    print("{a} + {b} = {result1}".format(a, b, add(a, b)))
    print("{a} - {b} = {result2}".format(a, b, sub(a, b)))
    print("{a} * {b} = {result3}".format(a, b, mul(a, b)))
    print("{a} / {b} = {result4}".format(a, b, div(a, b)))
    