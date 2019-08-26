#!/usr/bin/python3
""" fetch to specific url"""

if __name__ == "__main__":
    import requests
    from sys import argv
    data = requests.get(argv[1])
    print(data.headers['X-Request-Id'])
