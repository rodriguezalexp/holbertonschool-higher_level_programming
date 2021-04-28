#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
b = number % 10
if number > 5:
    print("Last digit of", number, "is {:d}".format(b),
          "and is greater than 5")
elif number == 0:
    print("Last digit of", number, "is {:d}".format(b),
          "and is 0")
else:
    print("Last digit of", number, "is {:d}".format(b),
          "and is less than 6 and not 0")
