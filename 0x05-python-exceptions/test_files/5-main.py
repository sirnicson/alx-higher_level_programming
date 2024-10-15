#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

# Test the raise_exception function
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
