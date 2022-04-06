def multiply_by_2(a_dict):
    new_dict = a_dict.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
