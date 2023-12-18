#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

   Args:
        my_list: a list can contain any type (integer, string, etc.)
        x: represents the number of elements to print

    Return:
        the real number of elements printed.
    """
    real_len = 0
    for i in range(x):
        try:
            print("{:d}".format(int(my_list[i])), end="")
            real_len += 1
        except (TypeError, ValueError):
            pass
        except NameError:
            break
    print("", end="\n")

    return real_len
