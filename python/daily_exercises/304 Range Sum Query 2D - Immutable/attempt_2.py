from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) + 1
        columns = len(matrix[0]) + 1

        self.pre_processed = [[0] * columns for row in range(rows)]

        for row in range(rows - 1):
            for column in range(columns - 1):
                self.pre_processed[row + 1][column + 1] = matrix[row][column] + self.pre_processed[row][column + 1] + self.pre_processed[row + 1][column] - self.pre_processed[row][column]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a_row = row1
        a_col = col1

        b_row = row1
        b_col = col2 + 1

        c_row = row2 + 1
        c_col = col1

        d_row = row2 + 1
        d_col = col2 + 1

        sum = self.pre_processed[d_row][d_col] - self.pre_processed[b_row][b_col] - self.pre_processed[c_row][c_col] + \
              self.pre_processed[a_row][a_col]
        return sum