#!/usr/bin/python3
def common_elements(set_1, set_2):
    return filter(lambda x:  x in set_2, list(set_1))
