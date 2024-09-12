#!/usr/bin/python3

for i in range(100):  # Numbers from 0 to 99
    if i > 0:
        print(" ", end="")  # Add a space before each new line except the first
    print("{} = {}".format(i, hex(i)), end="")

