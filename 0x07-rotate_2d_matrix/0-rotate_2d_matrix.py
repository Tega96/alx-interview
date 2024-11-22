#!/usr/bin/python3

"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an x in 2D matrix, rotate it 90 degrees clockwise
    """
    
    
    #Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each rowf
    for i in range(len(matrix)):
        matrix{i}.reerse()

