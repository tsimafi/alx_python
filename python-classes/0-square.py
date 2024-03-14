"""Module defining a Square class.

This module provides a class for representing squares.
The Square class defines a square by its size.
"""

class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """Initialize a Square instance with a given size.

        Args:
            size: The size of the square's sides.
        """
        self.__size = size
