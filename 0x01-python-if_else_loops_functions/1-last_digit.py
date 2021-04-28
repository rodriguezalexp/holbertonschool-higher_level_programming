#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
b = number % 10
if b > 5:
    print("Last digit of" number, "is {:d}".format(b),
          "and is greater than 5")
elif b == 0:
    print("Last digit of" number, "is {:d}".format(b),
          "and is 0")
elif b < 6 and b != 0:
    print("Last digit of" number, "is {:d}".format(b),
          "and is less than 6 and not 0")
