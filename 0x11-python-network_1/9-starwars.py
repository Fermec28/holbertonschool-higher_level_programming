#!/usr/bin/python3
""" request to star wars api"""
if __name__ == "__main__":
    import requests
    from sys import argv
    URL = "https://swapi.co/api/people"
    PARAMS = {'search': argv[1]}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    print("Number of results: {}".format(data['count']))
    for result in data['results']:
        print(result['name'])
