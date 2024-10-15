#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """Initialization of the MagicClass."""
    def __init__(self, radius=0):
        """Initialization of the data."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculation of the area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference."""
        return 2 * math.pi * self.__radius
