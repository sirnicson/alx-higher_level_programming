#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

# Test cases

# Case 1: x is less than the length of the list
print("Expected Output: 1 2 3")
num = safe_print_list([1, 2, 3, 4, 5], 3)
print("Returned:", num)  # Expected: 3

# Case 2: x is equal to the length of the list
print("\nExpected Output: 1 2 3 4 5")
num = safe_print_list([1, 2, 3, 4, 5], 5)
print("Returned:", num)  # Expected: 5

# Case 3: x is larger than the length of the list
print("\nExpected Output: 1 2 3 4 5")
num = safe_print_list([1, 2, 3, 4, 5], 7)
print("Returned:", num)  # Expected: 5

# Case 4: Empty list
print("\nExpected Output: ")
num = safe_print_list([], 5)
print("Returned:", num)  # Expected: 0

