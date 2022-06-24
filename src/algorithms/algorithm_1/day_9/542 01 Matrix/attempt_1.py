import math
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        distance_matrix = [[math.inf]*columns for row in range(rows)]

        for row in range(0, rows):
            for column in range(0, columns):
                if mat[row][column] == 0:
                    distance_matrix[row][column] = 0
                else:
                    if row > 0:
                        distance_matrix[row][column] = min(distance_matrix[row][column], distance_matrix[row - 1][column] + 1)
                    if column > 0:
                        distance_matrix[row][column] = min(distance_matrix[row][column], distance_matrix[row][column - 1] + 1)

        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                if row < rows - 1:
                    distance_matrix[row][column] = min(distance_matrix[row][column], distance_matrix[row + 1][column] + 1)
                if column < columns - 1:
                    distance_matrix[row][column] = min(distance_matrix[row][column], distance_matrix[row][column + 1])

        return distance_matrix
