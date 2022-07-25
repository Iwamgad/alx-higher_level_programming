#!/usr/bin/python3
"""
    My matrix division module
"""

def matrix_divided(matrix, div):
    """Divide all element of a matrix
    Args:
        matrix(list): A list of lists of int/floats
        div(int or float): The divisor
    Raises:
        TypeError:  If matrix is not a list of lists of integers or floats
                    If each row of the matrix are not of the same size
                    If div must be a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    Returns:
        matrix(list): A new matrix with all the elements divided
    """
    # Checks if the matrix is a list
    if not type(matrix) is list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    # Getting the length of the first list in the matrix
    if type(matrix[0]) is list:
        rowLength = len(matrix[0])
    # Running through the matrix
    for Lists in matrix:
        # Checks if each elements of the matrix is a list
        if not type(Lists) is list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        # Checks if the length of each row is the same
        if len(Lists) != rowLength:
            raise TypeError("Each row of the matrix must have the same size")
        # Checks if the elements in each lists of the matrix are int or float
        for elements in Lists:
            if not type(elements) is (int or float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    # Checks if div is a number
    if not type(div) is (int or float):
        raise TypeError("div must be a number")
    # Checks if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Dividing each elements of the lists of the matrix and creating a new one
    retMatrix = [[round(index / div, 2) for index in Lists] for Lists in matrix]

    return retMatrix
