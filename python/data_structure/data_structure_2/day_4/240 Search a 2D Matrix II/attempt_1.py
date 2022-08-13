from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        row = n - 1
        column = 0

        while row < n and row >= 0 and column < m and column >= 0:

            cur_num = matrix[row][column]

            if cur_num == target:
                return True

            elif cur_num < target:
                column += 1

            else:
                row -= 1

        return False

