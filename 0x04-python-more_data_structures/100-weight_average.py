#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return multiply_elements(my_list) / sum_elements(my_list)
    else:
        return 0


def multiply_elements(my_list=[]):
    aux = 0
    for x in my_list:
        aux += x[0] * x[1]
    return aux


def sum_elements(my_list=[]):
    aux = 0
    for x in my_list:
        aux += x[1]
    return aux
