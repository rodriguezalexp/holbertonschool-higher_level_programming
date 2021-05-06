#!/usr/bin/python3
from sys import argv

l = len(argv)

if l <= 2 and l != 0:
    print("{:d} {:s}".format(l - 1, "argument."))

else:
    print("{:d} {:s}".format(l - 1, "arguments:"))

for i, s in enumerate(argv):
    if i > 0:
        print("{:d}: {:s}".format(i, s))
