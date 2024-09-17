# 0x02. Python - Import & Modules

This project contains several Python scripts that demonstrate the use of modules, imports, and command-line arguments in Python.

## Files

### 0. Import a Simple Function from a Simple File
- **File**: `0-add.py`
- **Description**: Imports the function `add(a, b)` from `add_0.py` and prints the result of `1 + 2`.
- **Usage**: `./0-add.py`

### 1. My First Toolbox!
- **File**: `1-calculation.py`
- **Description**: Imports functions from `calculator_1.py` and performs basic arithmetic operations (addition, subtraction, multiplication, division).
- **Usage**: `./1-calculation.py`

### 2. How to Make a Script Dynamic!
- **File**: `2-args.py`
- **Description**: Prints the number of arguments and their values provided via the command line.
- **Usage**: `./2-args.py [arguments]`

### 3. Infinite Addition
- **File**: `3-infinite_add.py`
- **Description**: Sums all command-line arguments provided and prints the result.
- **Usage**: `./3-infinite_add.py [numbers]`

### 4. Who Are You?
- **File**: `4-hidden_discovery.py`
- **Description**: Prints the names defined in the compiled module `hidden_4.pyc`, excluding those starting with `__`.
- **Usage**: `./4-hidden_discovery.py`

### 5. Everything Can Be Imported
- **File**: `5-variable_load.py`
- **Description**: Imports the variable `a` from `variable_load_5.py` and prints its value.
- **Usage**: `./5-variable_load.py`

### 6. Build My Own Calculator!
- **File**: `100-my_calculator.py`
- **Description**: Imports all functions from `calculator_1.py` to perform basic arithmetic operations based on user input from the command line.
- **Usage**: `./100-my_calculator.py a operator b`
  - Operators: `+`, `-`, `*`, `/`

### 7. Easy Print
- **File**: `101-easy_print.py`
- **Description**: Prints `#pythoniscool` using an alternative method.
- **Usage**: `./101-easy_print.py`

### 8. ByteCode -> Python #3
- **File**: `102-magic_calculation.py`
- **Description**: Defines a function `magic_calculation(a, b)` that matches a given Python bytecode.
- **Usage**: This file is intended to be used with specific bytecode.

## Requirements

- All files are to be interpreted/compiled using Python 3.8.5 on Ubuntu 20.04 LTS.
- Files should end with a new line.
- The first line of each file should be `#!/usr/bin/python3`.
- Code should adhere to PEP 8 style guide using `pycodestyle` (version 2.8.*).
- All files must be executable.
- The length of files will be tested using `wc`.

## How to Run

1. Ensure Python 3.8.5 is installed.
2. Make sure each script has executable permissions:
```bash
   chmod +x <script_name>
```bash
