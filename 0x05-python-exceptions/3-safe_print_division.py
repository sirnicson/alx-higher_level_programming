#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Attempt to divide a by b
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        # Print the result (or None if division failed)
        print("Inside result: {}".format(result))
    return result
