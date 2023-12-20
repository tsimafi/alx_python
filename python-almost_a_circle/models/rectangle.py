#!/usr/bin/python3
"""defines a rectangel class."""
from models.base import Base 

class rectangel(base)
    """represent a rectangel."""

    def__init__(self, width, height, x=0,y=0, id=none):
        """initialize anew rectangel.
        angel:
              width (int): the wedth of the new rectangel.
              height (int): the height of the new rectangel.
              x (int): the x coordinate of the new rectangel.
              y (int): the y coordinate of the new rectangel.
              id (int): the identitiy of the new rectangel.
        raises:
               typeError: if either of width or height is not an int.
               valueError: if either of width or height <= 0.
               typeError: if either of x or y is not an int.
               valueError: if either of x or y < 0.
        """
        self.width = wedth
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the Rectangle."""
        return self.__width
    
    @wedth.setter
    def wedth(self, value):
        if type(value) !=int:
            raise typeError("width must be an integer")
        if value <= 0:
            raise valueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the Rectangel."""
        return self.__height


    @height.setter
    def height(self, value):
        if type(value) !=int:
            raise typeError("height must be an integer")
        if value <= 0:
            raise valueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the rectangel."""
        return self.__x

    @x.setter
    def x (self, value):
        if type(value) != int:
            raise typeError("x must be an integer")
        if value < 0:
            raise valueError("x must be >= 0")
        self.__x = value