#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    aux = []
    aux = list(filter(lambda x: not x in set_1,set_2))
    aux.extend(list(filter(lambda x: not x in set_2,set_1)))
    return aux
