# 0x08. Python - More Classes and Objects

## Project Overview
This project involves creating a series of classes that define a rectangle using Python. The classes are built step by step, starting with a simple empty class and adding features such as properties, methods, and instance tracking.

## Requirements
- **Editors**: Allowed editors are `vi`, `vim`, and `emacs`.
- **Python Version**: All files must be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- **File Format**: All files should end with a new line and the first line of all files should be exactly `#!/usr/bin/python3`.
- **Code Style**: Code must conform to `pycodestyle` (version 2.8.*).
- **Executable**: All files must be executable.
- **File Length**: The length of your files will be tested using `wc`.

## File Descriptions
The project consists of the following Python files, each implementing specific tasks related to the rectangle class:

1. **`0-rectangle.py`**
   - An empty class `Rectangle` that defines a rectangle.

2. **`1-rectangle.py`**
   - A class `Rectangle` that includes:
     - Private instance attributes `width` and `height`.
     - Property methods to retrieve and set these attributes, enforcing type and value constraints.

3. **`2-rectangle.py`**
   - Extends the `Rectangle` class by adding methods:
     - `area()`: Returns the area of the rectangle.
     - `perimeter()`: Returns the perimeter of the rectangle, handling cases where width or height is zero.

4. **`3-rectangle.py`**
   - Adds string representation functionality:
     - `__str__()`: Returns a string that represents the rectangle using the `#` character.

5. **`4-rectangle.py`**
   - Introduces `__repr__()` to provide a string representation that can recreate a new instance using `eval()`.

6. **`5-rectangle.py`**
   - Modifies the class to print a message when an instance is deleted and ensures proper management of the instance count.

7. **`6-rectangle.py`**
   - Enhances the `Rectangle` class by adding a class attribute `number_of_instances`, which tracks the number of instances created.

8. **`7-rectangle.py`**
   - Introduces the class attribute `print_symbol`, which allows customization of the symbol used for the string representation of the rectangle.

9. **`8-rectangle.py`**
   - Implements additional features, including:
     - Handling custom print symbols.
     - Ensuring all constraints from previous tasks are maintained.

10. **`9-rectangle.py`**
    - Final enhancements that might include additional methods or functionalities, such as comparing rectangles or other operations.

11. **`101-nqueens.py`**
    - A program that solves the N queens problem.

## Usage
To use this project, ensure that you have Python 3 installed on your Ubuntu system. Run the scripts directly from the terminal, making sure to set executable permissions:

```bash
chmod +x filename.py
./filename.py

