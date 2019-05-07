#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx < len(copy) and idx >= 0:
        copy[idx] = element
    return copy
