#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to print the value using the specified format
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If there's a ValueError or TypeError, return False
        return False
