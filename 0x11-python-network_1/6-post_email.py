#!/usr/bin/python3
""" post to specific url"""

if __name__ == "__main__":
    import requests
    from sys import argv
    data = {'email': argv[2]}
    response = requests.post(url=argv[1], data=data)
    print(response.text)
