#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ A class that defines a square with a private attribute size """

    def __init__(self, size=0):
        """ Initializes the square with an optional size """
        self.size = size  # Use the setter to validate the size

    @property
    def size(self):
        """ Property getter to retrieve the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Property setter to set the size with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2
