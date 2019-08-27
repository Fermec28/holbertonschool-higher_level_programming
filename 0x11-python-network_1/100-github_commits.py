#!/usr/bin/python3
""" get id form github """
if __name__ == "__main__":
    import requests
    from sys import argv
    req = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    print(req)
    res = requests.get(req)
    i = 1
    for commit in res.json():
        print("{}: {}".format(commit["sha"], commit["commit"]["author"]["name"]))
        if i == 10:
            break
        i += 1
