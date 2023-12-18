#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists.

    Args:
        my_list_1, my_list_2: lists of integer
        list_length: length of sencode list

    Return:
        a new list (length = list_length) with all divisions
    """
    result = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            val = 0
            print("division by 0")
        except (TypeError, ValueError):
            val = 0
            print("wrong type")
        except IndexError:
            val = 0
            print("out of range")
        finally:
            result.append(val)
    return result
