#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        """
        Raise an exception is area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate that value is an integer.

        Args:
            name (): name of the parameter
            value (_type_): value to be validated

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not an integer.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
