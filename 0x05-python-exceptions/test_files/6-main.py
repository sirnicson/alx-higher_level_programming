#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

# Test the raise_exception_msg function
try:
    raise_exception_msg("This is a name exception message")
except NameError as e:
    print("Caught an exception:", e)
