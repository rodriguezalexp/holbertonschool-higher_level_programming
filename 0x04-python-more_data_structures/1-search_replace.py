#!/usr/bin/python3
def search_replace(my_list, search, replace):
    aux = []
    for i in my_list:
        if i == search:
            aux.append(replace)
        else:
            aux.append(i)
    return aux
