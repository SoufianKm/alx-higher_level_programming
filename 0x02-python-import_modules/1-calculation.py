#!/usr/bin/python3
if __name__ == "__main__":
    """does some  Maths of 10 and 5, and prints the result"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    operators = ['+', '-', '*', '/']
    maths = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    for i in range(len(operators)):
        print("{} {} {} = {}".format(a, b, operators[i], maths[i]))
