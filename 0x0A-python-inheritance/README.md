# 0x0A. Python - Inheritance

## Project Overview
This project focuses on understanding and implementing inheritance in Python. Through various tasks, we will explore how classes can inherit attributes and methods from other classes, thereby promoting code reuse and organization.

## Objectives
- Gain hands-on experience with class inheritance in Python.
- Implement custom classes with extended functionalities.
- Develop skills in writing test cases and documenting code effectively.

## File Structure
- `0-lookup.py`: Function to return the list of available attributes and methods of an object.
- `1-my_list.py`: Class `MyList` that inherits from `list`.
- `2-is_same_class.py`: Function to check if an object is an instance of a specific class.
- `3-is_kind_of_class.py`: Function to check if an object is an instance of, or inherited from, a specified class.
- `4-inherits_from.py`: Function to verify if an object is an instance of a class that inherited from a specified class.
- `5-base_geometry.py`: Empty class `BaseGeometry`.
- `6-base_geometry.py`: Class `BaseGeometry` with an area method raising an exception.
- `7-base_geometry.py`: Class with integer validation for geometric shapes.
- `8-rectangle.py`: Class `Rectangle` inheriting from `BaseGeometry`.
- `9-rectangle.py`: Rectangle class with string representation and area calculation.
- `10-square.py`: Class `Square` inheriting from `Rectangle`.
- `11-square.py`: Extended `Square` class.
- `100-my_int.py`: Class `MyInt` with inverted equality.
- `101-add_attribute.py`: Function to add new attributes to objects.

## Requirements
- Python 3.8.5
- All files should end with a new line.
- Use the `pycodestyle` (version 2.8.*) for coding style checks.
- Each module and method must have corresponding documentation.

## Usage
Run each Python script to implement the functionality described in the respective files. Test cases can be executed using:
```bash
python3 -m doctest ./tests/*

