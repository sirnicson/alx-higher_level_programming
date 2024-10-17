#!/usr/bin/python3
"""Creating a base class"""

import json
import csv
import os


class Base:
    """Defining class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning json string representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format and saves it to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is not None:
                fieldnames = ['id']
                if cls.__name__ == 'Rectangle':
                    fieldnames.extend(['width', 'height', 'x', 'y'])
                elif cls.__name__ == 'Square':
                    fieldnames.extend(['size', 'x', 'y'])
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([o.to_dictionary() for o in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of instances from CSV format."""
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, newline='') as f:
                reader = csv.DictReader(f)
                return [cls.create(**{key: int(value) for key, value in row.items()})
                        for row in reader]
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A static method that opens a window and draws all the instances"""

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for shape in list_rectangles + list_squares:
            t.penup()
            t.setpos(shape.x, shape.y)
            t.pendown()
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, shape)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle or Square."""
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
