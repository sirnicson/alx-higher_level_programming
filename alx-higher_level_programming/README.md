# JavaScript - Objects, Scopes, and Closures

## Overview
This project explores advanced concepts in JavaScript, including classes, objects, and closures. The goal is to deepen understanding of JavaScript's prototype-based structure, function bundling (closures), and class manipulation.

---

## Tests ✔️
**Folder:** `tests`

Contains test files to verify the correctness of implemented functions and scripts.

---

## Function Prototypes 💾
The following are the prototypes for the functions implemented in this project:

| File               | Prototype                                      |
|--------------------|------------------------------------------------|
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.esrever = function (list)`           |
| `9-logme.js`       | `exports.logMe = function (item)`             |
| `10-converter.js`  | `exports.converter = function (base)`         |

---

## Tasks 📃

### 0. Rectangle #0
**File:** `0-rectangle.js`
- Defines an empty class `Rectangle`.

### 1. Rectangle #1
**File:** `1-rectangle.js`
- Defines a class `Rectangle` with a constructor to initialize instance attributes `width` and `height` with parameters `w` and `h`.

### 2. Rectangle #2
**File:** `2-rectangle.js`
- Builds on `1-rectangle.js`.
- Creates an empty object if `w` or `h` is less than or equal to 0.

### 3. Rectangle #3
**File:** `3-rectangle.js`
- Builds on `2-rectangle.js`.
- Adds an instance method `print()` that prints the rectangle using the `X` character.

### 4. Rectangle #4
**File:** `4-rectangle.js`
- Builds on `3-rectangle.js`.
- Adds:
  - `rotate()`: Swaps the width and height of the rectangle.
  - `double()`: Doubles the width and height of the rectangle.

### 5. Square #0
**File:** `5-square.js`
- Defines a class `Square` that inherits from `Rectangle`.
- Constructor takes one argument `size`.

### 6. Square #1
**File:** `6-square.js`
- Builds on `5-square.js`.
- Adds an instance method `charPrint(c)` to print the square using the character `c`. Defaults to `X` if `c` is undefined.

### 7. Occurrences
**File:** `7-occurrences.js`
- Function that returns the number of occurrences of `searchElement` in a `list`.

### 8. Esrever
**File:** `8-esrever.js`
- Function that reverses a list.

### 9. Log me
**File:** `9-logme.js`
- Function that prints the number of arguments already printed and the value of the new argument.
  - Output format: `<number arguments already printed>: <current argument value>`

### 10. Number conversion
**File:** `10-converter.js`
- Function that converts a number from base 10 to another base passed as an argument.

### 11. Factor index
**File:** `100-map.js`
- Imports an array and creates a new array where each value is the value of the initial list multiplied by its index.
- Prints both the initial and new arrays.

### 12. Sorted occurrences
**File:** `101-sorted.js`
- Imports a dictionary of occurrences by user ID.
- Computes and prints a new dictionary of user IDs sorted by occurrences.

### 13. Concat files
**File:** `102-concat.js`
- Concatenates two files passed as arguments into a third file.
- Usage: `./102-concat.js fileA fileB fileC`.

---


## Usage
To execute the scripts or test the functions, use the Node.js runtime. Example:
```bash
node <script_name>
