#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function

def divide(a, b):
    return a / b

def add(a, b):
    return a + b

# Test cases for the function
print("Result of divide: {}".format(safe_function(divide, 10, 2)))  # Expected: 5.0
print("Result of divide: {}".format(safe_function(divide, 10, 0)))  # Expected: None, prints Exception: division by zero
print("Result of add: {}".format(safe_function(add, 10, 5)))        # Expected: 15

