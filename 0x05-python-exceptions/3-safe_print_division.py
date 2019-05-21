#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        b = "{:.1f}".format(a / b)
        return b
    except:
        b = "None"
        return None
    finally:
        print("Inside result: {}".format(b))
