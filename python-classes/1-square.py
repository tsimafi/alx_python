class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is negative.
    """

    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
