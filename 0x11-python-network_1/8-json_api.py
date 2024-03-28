#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    try:
        response = post(URL, data)

        if response.headers['content-type'] == 'application/json':
            res = response.json()
            if (res == {} or res == 0):
                print('No result')
            else:
                print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print('Not a valid JSON')
    except Exception as err:
        pass
