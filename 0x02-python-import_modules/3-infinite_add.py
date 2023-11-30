#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys
    res = 0
    if len(sys.argv) > 2:
        for i in range(1, len(sys.argv)):
            res += int(sys.argv[i])
        print("{}".format(res))

