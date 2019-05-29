#!/usr/bin/python3
def magic_string(paulist=[0]):
    paulist[0] += 1
    return ("Holberton, " * paulist[0])[:-2]
