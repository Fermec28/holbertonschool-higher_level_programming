#!/usr/bin/python3
for number in range(0,99):
    print("{:d}{:d}".format(int(number/10), int(number%10)), end=", ")
print(99)
