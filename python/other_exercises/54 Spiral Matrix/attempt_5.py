from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left = 0
        right = len(matrix[0]) - 1

        up = 0
        down = len(matrix) - 1

        res = []

        while (left <= right) and (up <= down):

            for column in range(left, right + 1, 1):
                res.append(matrix[up][column])
            up += 1

            for row in range(up, down + 1, 1):
                res.append(matrix[row][right])
            right -= 1

            for column in range(right, left - 1, -1):
                res.append(matrix[down][column])
            down -= 1

            for row in range(down, up - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res[:len(matrix)*len(matrix[0])]
