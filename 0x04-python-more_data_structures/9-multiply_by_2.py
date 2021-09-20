#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    print(cpy)
    for key in cpy:
        cpy[key] *= 2
    return(cpy)
