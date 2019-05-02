#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

str = "Last digit of {:d} is".format(number)
str = "{:s} {:d}".format(str, last_digit)
if last_digit > 5:
    print("{:s} and is greater than 5".format(str))
elif last_digit == 0:
    print("{:s} and is 0".format(str))
elif (last_digit < 6 and last_digit != 0):
    print("{:s} and is less than 6 and not 0".format(str))
