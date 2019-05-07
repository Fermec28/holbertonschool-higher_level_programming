#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    aux = my_list[:]
    aux.reverse()
    for i in aux:
        print("{:d}".format(i))
