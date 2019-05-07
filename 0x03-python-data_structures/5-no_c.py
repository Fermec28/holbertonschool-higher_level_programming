#!/usr/bin/python3
def no_c(my_string):
    aux = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            aux += x
    return aux
