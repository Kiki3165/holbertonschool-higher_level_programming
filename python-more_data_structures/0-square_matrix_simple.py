#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return map(pow, matrix, [2]*len(matrix))
