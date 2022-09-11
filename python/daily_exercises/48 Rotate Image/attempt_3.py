import math
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(rows):
            for column in range(row, columns):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

        for row in range(rows):
            for column in range(math.ceil(columns / 2)):
                matrix[row][column], matrix[row][columns - 1 - column] = matrix[row][columns - 1 - column], matrix[row][column]

        return matrix
