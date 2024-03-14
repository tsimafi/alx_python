"""Module defining a Square class.

This module provides a class for representing squares.
The Square class defines a square by its size and provides methods for calculating its area.
"""

class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
