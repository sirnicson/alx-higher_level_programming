#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    MyList is a subclass of list that includes a method to print the list sorted.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)  # Use the built-in sorted function
        print(sorted_list)
