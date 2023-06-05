import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        dp = [[math.inf]*m for _ in range(n)]

        for row in range(n):
            for column in range(m):
                if mat[row][column] == 0:
                    dp[row][column] = 0
                else:
                    if row > 0:
                        dp[row][column] = min(dp[row][column], dp[row-1][column])
                    if column > 0:
                        dp[row][column] = min(dp[row][column], dp[row][column-1])

        for row in range(n-1, -1, -1):
            for column in range(m-1, -1, -1):
                if row < (n-1):
                    dp[row][column] = min(dp[row][column], dp[row+1][column])

                if column < (m-1):
                    dp[row][column] = min(dp[row][column], dp[row][column+1])

        return dp

