#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_list = a_dictionary.copy()

    cpy_list.update((x, y*2) for x, y in cpy_list.items())
    return cpy_list


"""for key in a_dictionary.keys():
        cpy = a_dictionary[key] * val
    return cpy
    cpy_list = [a_dictionary[x] * 2 for x in a_dictionary]
    return dict(cpy_list)
    return [[round(i / div, 2) for i in l] for l in matrix]"""
