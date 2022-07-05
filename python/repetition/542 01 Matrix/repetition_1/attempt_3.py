import math
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        dp = [[math.inf]*columns for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):

                if mat[row][column] == 0:
                    dp[row][column] = 0
                else:
                    if row > 0:
                        dp[row][column] = min(dp[row][column], dp[row-1][column] + 1)
                    if column > 0:
                        dp[row][column] = min(dp[row][column], dp[row][column-1] + 1)

        for row in range(rows -1, -1, -1):
            for column in range(columns -1, -1, -1):

                if row < rows - 1:
                    dp[row][column] = min(dp[row][column], dp[row+1][column] + 1)
                if column < columns - 1:
                    dp[row][column] = min(dp[row][column], dp[row][column+1] + 1)

        return dp