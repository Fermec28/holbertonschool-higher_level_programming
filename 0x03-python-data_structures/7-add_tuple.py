#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arr = [0, 0]
    for x in range(2):
        if x < len(tuple_a):
            arr[x] += tuple_a[x]
        if x < len(tuple_b):
            arr[x] += tuple_b[x]
    return (arr[0], arr[1])
