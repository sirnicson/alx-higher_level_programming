#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ Defining a class square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the data. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size to a value. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieves the position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position to a value. """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the current square area. """
        return self.__size ** 2

    def my_print(self):
        """ Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
