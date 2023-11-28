#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(number):
    if number < 0:
        last_digit = ((number * (-1)) % 10) * (-1)
    else:
        last_digit = number % 10
    if last_digit > 5:
        stat = "greater than 5"
    elif last_digit < 6 and not(last_digit == 0):
        stat = "less than 6 and not 0"
    elif last_digit == 0:
        stat = "0"
    print("Last digit of {} is {} and is {}".format(number, last_digit, stat))
