#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

# Test cases
print("Test Case 1:")
my_list_1 = [10, 20, 30, 40]
my_list_2 = [2, 0, "hello", 4]
result = list_division(my_list_1, my_list_2, 4)
print("Result:", result)  # Expected: [5.0, 0, 0, 10.0]

print("\nTest Case 2:")
my_list_1 = [5, 6]
my_list_2 = [2, 3]
result = list_division(my_list_1, my_list_2, 3)
print("Result:", result)  # Expected: [2.5, 2.0, 0] (out of range for index 2)

print("\nTest Case 3:")
my_list_1 = [100, "a", 20]
my_list_2 = [10, 5, 2]
result = list_division(my_list_1, my_list_2, 3)
print("Result:", result)  # Expected: [10.0, 0, 10.0]
