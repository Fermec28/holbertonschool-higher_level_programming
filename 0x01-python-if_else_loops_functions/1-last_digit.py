#!/usr/bin/python3
import random
number = random.randint(-10000, -1)
str = "Last digit of {:d} is".format(number)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
str = "{} {:d}".format(str, last_digit)
if last_digit > 5:
    print("{} and is greater than 5".format(str))
elif last_digit == 0:
    print("{} and is 0".format(str))
elif (last_digit < 6 and last_digit != 0):
    print("{} and is less than 6 and not 0".format(str))
