#!/usr/bin/python3
if __name__ == "__main__":
    hidden_4 = __import__('hidden_4').hidden_4

    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{:s}".format(i))
