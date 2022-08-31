from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        columns = len(matrix)
        rows = len(matrix[0])

        for column in range(columns):
            for row in range(column, rows, 1):
                matrix[column][row], matrix[row][column] = matrix[row][column], matrix[column][row]

        for row in range(rows):
            for position in range(columns // 2):
                matrix[row][position], matrix[row][columns - position - 1] = matrix[row][columns - position - 1], matrix[row][position]

