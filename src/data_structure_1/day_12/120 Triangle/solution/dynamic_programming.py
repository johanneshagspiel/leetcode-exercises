from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_rows = len(triangle)

        for row in range(n_rows - 2, -1, -1):
            n_col = triangle[row]

            for col in range(n_col):
                triangle[row][col] = triangle[row][col] + min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]