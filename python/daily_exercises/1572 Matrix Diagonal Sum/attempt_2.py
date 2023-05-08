import math


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        matSize = len(mat)
        cellIndex = 0
        sum = 0

        while cellIndex < matSize:
            sum += mat[cellIndex][cellIndex]
            cellIndex += 1

        row = 0
        column = cellIndex - 1
        while column > -1:
            if row != column:
                sum += mat[row][column]
            column -= 1
            row += 1

        return sum
