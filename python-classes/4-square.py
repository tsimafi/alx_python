'''This module defines a Square class representing a square shape.'''

class Square:
    '''A class to represent a square.

    Attributes:
        size (int): The size of the square.
    '''

    def __init__(self, size=0):
        '''Initialize the Square object.

        Args:
            size (int): The size of the square (default 0).
        '''
        self.size = size

    @property
    def size(self):
        '''int: The size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Calculate the area of the square.

        Returns:
            int: The area of the square.
        '''
        return self.size ** 2

    def my_print(self):
        '''Print the square using '#' character.

        If size is 0, prints an empty line.
        '''
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
