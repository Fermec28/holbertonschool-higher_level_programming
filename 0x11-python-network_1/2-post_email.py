#!/usr/bin/python3
""" make post request with urllib"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
