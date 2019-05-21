#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            i += 1
            print("{:d}".format(my_list[j]), end="")
        except (ValueError, TypeError):
            i -= 1
    print("")
    return i
