#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    URL = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]

    res = requests.get(URL, auth=(username, password))
    print(res.json().get('id'))
