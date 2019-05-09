#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    aux_dic = a_dictionary.copy()
    for key in aux_dic.keys():
        aux_dic[key] *=2
    return aux_dic
