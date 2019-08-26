#!/usr/bin/python3
""" Take header from request"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
