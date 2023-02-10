#!/usr/bin/python3
'''def'''


def pascal_triangle(n):
    'def'
    if n <= 0:
        return []

    triangle = []
    current_row = [1]
    for i in range(n):
        triangle.append(current_row)
        current_row = [1] + [current_row[j] + current_row[j - 1]
                             for j in range(1, len(current_row))] + [1]

    return triangle
