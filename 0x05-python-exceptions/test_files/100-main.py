#!/usr/bin/python3
safe_print_integer_err = __import__('100-safe_print_integer_err').safe_print_integer_err

# Test cases for the function
print(safe_print_integer_err(42))         # Expected: True, prints 42
print(safe_print_integer_err("Not int"))  # Expected: False, prints Exception:...
print(safe_print_integer_err(3.14))       # Expected: False, prints Exception:...
