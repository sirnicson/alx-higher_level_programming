#!/usr/bin/python3
"""Create Square class."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if this square's area equals the other's."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if this square's area not equals the other's."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if this square's area greater than the other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area greater or equal."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Return True if this square's area less than the other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area less than or equal."""
        return self.area() <= other.area()
