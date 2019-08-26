#!/usr/bin/python3
""" get id form github """
if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if res.json() and res.status_code == 200:
        print(res.json()['id'])
    else:
        print("None")
