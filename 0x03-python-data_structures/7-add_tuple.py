#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arr = [0, 0]
    for x in range(2):
        if tuple_a[x]:
            arr[x] += tuple_a[x]
        if tuple_b[x]:
            arr[x] += tuple_b[x]
    return (arr[0], arr[1])
