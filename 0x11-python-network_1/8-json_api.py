#!/usr/bin/python3
""" request to api  """

if __name__ == "__main__":
    import requests
    from sys import argv
    data = {'q': ""}
    if len(argv) > 1:
        data['q'] = argv[1]
    response = requests.post(url="http://0.0.0.0:5000/search_user", data=data)
    try:
        data_response = eval(response.text)
        if data_response:
            print("[{}] {}".format(data_response['id'], data_response['name']))
        else:
            print("No result")
    except Exception as err:
        print("Not a valid JSON")
