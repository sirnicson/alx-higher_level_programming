#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

# Test cases
print("Expected Output: 42")
result = safe_print_integer(42)
print("Returned:", result)  # Expected: True

print("\nExpected Output: -10")
result = safe_print_integer(-10)
print("Returned:", result)  # Expected: True

print("\nExpected Output: 3.14")
result = safe_print_integer(3.14)
print("Returned:", result)  # Expected: False

print("\nExpected Output: Hello")
result = safe_print_integer("Hello")
print("Returned:", result)  # Expected: False

print("\nExpected Output: None")
result = safe_print_integer(None)
print("Returned:", result)  # Expected: False

