from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        row = n - 1
        column = 0

        while row >= 0 and row < n and column >= 0 and column < m:

            num = matrix[row][column]

            if num == target:
                return True

            elif num < target:
                column += 1

            else:
                row -= 1

        return False

