#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ A class that defines a square with a private attribute size """

    def __init__(self, size):
        """ Initializes the square with the given size """
        self.__size = size  # Private instance attribute
