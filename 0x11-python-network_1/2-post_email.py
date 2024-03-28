#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    try:
        DATA = urllib.parse.urlencode({"email": sys.argv[2]})
        DATA = DATA.encode('ascii')

        with urllib.request.urlopen(sys.argv[1], DATA) as response:
            print(response.read().decode('utf-8'))
    except Exception as err:
        pass
