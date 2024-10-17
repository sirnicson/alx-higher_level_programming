#!/usr/bin/python3
"""Module that defines the Base class"""

class Base:
    """Base class for all future classes in the project.
    Manages the 'id' attribute to avoid duplication."""
    
    __nb_objects = 0  # Private class attribute to keep track of object count

    def __init__(self, id=None):
        """Initializes the Base class.
        Args:
            id (int, optional): If provided, sets the id to the passed value. Otherwise, increments __nb_objects and assigns a unique id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
