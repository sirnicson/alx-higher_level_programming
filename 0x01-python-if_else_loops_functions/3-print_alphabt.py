#!/usr/bin/python3

for i in range(97, 123):  # ASCII values for 'a' to 'z'
    if chr(i) != 'e' and chr(i) != 'q':
        print(chr(i), end="")
