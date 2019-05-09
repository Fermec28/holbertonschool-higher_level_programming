#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(set(my_list[:]))
    num = 0
    for el in my_list:
        num += el
    return num
