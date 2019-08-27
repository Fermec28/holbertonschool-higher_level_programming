#!/usr/bin/python3
""" request to star wars api"""


def handler_request(URL="", PARAMS=""):
    """ function call request"""
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    if PARAMS:
        print("Number of results: {}".format(data['count']))
    for result in data['results']:
        print(result['name'])
    if data["next"]:
        handler_request(data["next"])

if __name__ == "__main__":
    import requests
    from sys import argv
    URL = "https://swapi.co/api/people"
    PARAMS = {'search': argv[1]}
    handler_request(URL, PARAMS)
