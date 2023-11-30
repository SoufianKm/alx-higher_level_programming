#!/usr/bin/python3
if __name__ == "__main__":
    """a calculator handles basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv) - 1
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a, b = int(sys.argv[1]), int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            exit(0)
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            exit(0)
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            exit(0)
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
