#!/usr/bin/python3*
def print_last_digit(number):
    last_digit = int(str(number)[-1])
    print(last_digit)
    last_digit = number % 10
    print(last_digit)