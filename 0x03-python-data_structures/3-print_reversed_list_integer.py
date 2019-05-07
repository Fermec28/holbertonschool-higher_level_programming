#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    aux = my_list[:]
    aux.reverse()
    if aux:
        for i in aux:
            print("{:d}".format(i))
