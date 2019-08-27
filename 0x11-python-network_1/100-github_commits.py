#!/usr/bin/python3
""" get id form github """
if __name__ == "__main__":
    import requests
    from sys import argv
    req = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = requests.get(req)
    i = 1
    for comit in res.json():
        print("{}: {}".format(comit["sha"], comit["commit"]["author"]["name"]))
        if i == 10:
            break
        i += 1
