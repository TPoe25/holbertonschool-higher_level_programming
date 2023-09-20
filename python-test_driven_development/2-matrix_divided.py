#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide a matrix by a scalar.

    Args: matrix (list): The matrix to divide.
        div (int or float): The scalar to divide by.
    
    Returns:
        list: A new matrix w/ all elements divided by the scalar.
    
    Raises:
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    Example:
        >>> matrix = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67 1.0], [1.33, 1.67 2.0]]
        """
        
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of ints/floats.")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an integer or float.")
    
    if div == 0:
        raise ZeroDivisionError("division by zero.")
    
    new_matrix = []
    
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
        
    return new_matrix