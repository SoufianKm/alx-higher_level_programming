#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys
    l = len(sys.argv) - 1
    if l == 0:
        print("{} arguments.".format(l))
    elif l == 1:
        print("{} argument:".format(l))
        print("{}: {}".format(l, sys.argv[l]))
    else:
        print("{} arguments:".format(l))
        for i in range(1, l + 1):
            print("{}: {}".format(i, sys.argv[i]))
