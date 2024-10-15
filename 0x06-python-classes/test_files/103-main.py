#!/usr/bin/python3
"""Test the MagicClass."""

from magic_class import MagicClass

def main():
    """Main function to test MagicClass."""
    # Test with valid radius
    magic1 = MagicClass(5)
    print(f"Radius: {magic1._MagicClass__radius}")
    print(f"Area: {magic1.area()}")
    print(f"Circumference: {magic1.circumference()}")

    # Test with float radius
    magic2 = MagicClass(3.5)
    print(f"Radius: {magic2._MagicClass__radius}")
    print(f"Area: {magic2.area()}")
    print(f"Circumference: {magic2.circumference()}")

    # Test with zero radius
    magic3 = MagicClass(0)
    print(f"Radius: {magic3._MagicClass__radius}")
    print(f"Area: {magic3.area()}")
    print(f"Circumference: {magic3.circumference()}")

    # Test with invalid radius
    try:
        magic4 = MagicClass("invalid")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()

