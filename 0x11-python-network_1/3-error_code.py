#!/usr/bin/python3
""" catching errors """
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
