#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = matrix.copy()

    for i in range(len(matrix)):
        sqr_matrix[i] = list(map(sqr, matrix[i]))

    return (sqr_matrix)

def sqr(n):
    return (n ** 2)
