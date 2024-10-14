#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

# Test cases
print("Test Case 1: 10 divided by 2")
result = safe_print_division(10, 2)
print("Returned:", result)  # Expected: 5.0

print("\nTest Case 2: 10 divided by 0")
result = safe_print_division(10, 0)
print("Returned:", result)  # Expected: None

print("\nTest Case 3: -8 divided by 4")
result = safe_print_division(-8, 4)
print("Returned:", result)  # Expected: -2.0

print("\nTest Case 4: 7 divided by 3")
result = safe_print_division(7, 3)
print("Returned:", result)  # Expected: 2.3333333333333335
