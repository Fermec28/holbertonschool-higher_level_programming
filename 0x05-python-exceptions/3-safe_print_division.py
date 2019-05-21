#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        b = "{:.1f}".format(a / b)
    except:
        b = "None"
    finally:
        print("Inside result {}".format(b))
        return b
