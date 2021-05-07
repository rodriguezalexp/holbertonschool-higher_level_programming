#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    aux = []
    for i in matrix:
        aux.append(list(map(lambda x: x ** 2, i)))
    return aux
