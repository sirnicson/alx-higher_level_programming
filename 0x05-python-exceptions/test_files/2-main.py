#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

# Test cases
my_list = [1, "Hello", 2, 3.14, 4, "World", 5]

print("Expected Output: 1 2 4 5")
result = safe_print_list_integers(my_list, 7)
print("Returned:", result)  # Expected: 4

print("\nExpected Output: 1 2")
result = safe_print_list_integers(my_list, 3)
print("Returned:", result)  # Expected: 2

print("\nExpected Output: ")
result = safe_print_list_integers(my_list, 0)
print("Returned:", result)  # Expected: 0

print("\nExpected Output: 1")
result = safe_print_list_integers(my_list, 1)
print("Returned:", result)  # Expected: 1

print("\nExpected Output: 1 2 4")
result = safe_print_list_integers(my_list, 5)
print("Returned:", result)  # Expected: 3
