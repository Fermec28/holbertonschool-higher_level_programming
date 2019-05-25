#!/usr/bin/python3
"""
This module contains a function todivide each element
"""


def matrix_divided(matrix, div):
    """
    Function to divide each element by div
    @matrix: matrix
    @div: number to divide
    Return: New matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(msg)
    new_matrix = []
    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
        if (len(row) != average_list(len_rows)):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(msg)
            else:
                new_row.append(round((elem / div), 2))
        new_matrix.append(new_row)
    return new_matrix


def average_list(list_i):
    """
    Funcion to calculate average of list
    @list: list
    Return: Average of list
    """
    average = 0
    for item in list_i:
        average += item
    return average / len(list_i)
