#!/usr/bin/python3
def uppercase(str):
    for c in str:
        scan = ord(c)
        if scan >= 97 and scan <= 122:
            c = chr(scan - 32)
        print("{}".format(c), end='')
    print("")
