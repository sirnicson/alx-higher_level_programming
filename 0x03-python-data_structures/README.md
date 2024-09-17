# 0x03. Python - Data Structures: Lists, Tuples

## Project Overview

This project covers fundamental Python data structures including lists and tuples. The tasks involve implementing functions to manipulate and process these data structures. The project is designed to deepen your understanding of Python’s list and tuple operations, as well as basic algorithmic concepts.

## Requirements

- Python version 3.8.5
- Files should end with a new line
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code must adhere to the `pycodestyle` version 2.8.*
- All header files should be include guarded
- All functions must be prototyped in header files called `lists.h`
- No global variables allowed
- Maximum of 5 functions per file

## Tasks

### 0. Print a list of integers
- **Prototype**: `def print_list_integer(my_list=[])`
- **Description**: Prints all integers of a list, one integer per line using `str.format()`.

### 1. Secure access to an element in a list
- **Prototype**: `def element_at(my_list, idx)`
- **Description**: Retrieves an element from a list at a specific index, with checks for negative and out-of-range indices.

### 2. Replace element
- **Prototype**: `def replace_in_list(my_list, idx, element)`
- **Description**: Replaces an element in a list at a specific position, with validation for negative and out-of-range indices.

### 3. Print a list of integers... in reverse!
- **Prototype**: `def print_reversed_list_integer(my_list=[])`
- **Description**: Prints all integers of a list in reverse order, one integer per line using `str.format()`.

### 4. Replace in a copy
- **Prototype**: `def new_in_list(my_list, idx, element)`
- **Description**: Replaces an element in a list at a specific position without modifying the original list.

### 5. Can you C me now?
- **Prototype**: `def no_c(my_string)`
- **Description**: Removes all characters 'c' and 'C' from a string.

### 6. Lists of lists = Matrix
- **Prototype**: `def print_matrix_integer(matrix=[[]])`
- **Description**: Prints a matrix of integers, with each row on a new line and integers separated by spaces.

### 7. Tuples addition
- **Prototype**: `def add_tuple(tuple_a=(), tuple_b=())`
- **Description**: Adds two tuples, returning a tuple with the sum of corresponding elements.

### 8. More returns!
- **Prototype**: `def multiple_returns(sentence)`
- **Description**: Returns a tuple with the length of a string and its first character.

### 9. Find the max
- **Prototype**: `def max_integer(my_list=[])`
- **Description**: Finds the largest integer in a list.

### 10. Only by 2
- **Prototype**: `def divisible_by_2(my_list=[])`
- **Description**: Returns a list of boolean values indicating whether each integer in the original list is divisible by 2.

### 11. Delete at
- **Prototype**: `def delete_at(my_list=[], idx=0)`
- **Description**: Deletes the item at a specific position in a list, handling negative and out-of-range indices.

## Usage

To test these functions, you can use the provided main files in the `main.py` files. Each main file demonstrates how to use the corresponding function and shows expected outputs.


