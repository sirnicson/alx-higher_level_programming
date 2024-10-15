#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ A class that defines a square with a private attribute size """

    def __init__(self, size=0):
        """ Initializes the square with an optional size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2
