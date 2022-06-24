from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        columns = len(matrix[0]) + 1
        rows = len(matrix) + 1

        self.dp = [[0] * columns for row in range(rows)]

        # calculate prefix sum
        for row in range(rows - 1):
            for column in range(columns - 1):
                self.dp[row + 1][column + 1] = matrix[row][column] + self.dp[row][column + 1] + self.dp[row + 1][column] - self.dp[row][column]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


if __name__ == '__main__':
    numMatrix = NumMatrix([[-1]]);
    result_1 = numMatrix.sumRegion(0, 0, 0, 0)
    print(result_1)
