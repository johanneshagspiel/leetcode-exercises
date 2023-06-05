from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        dp = [[math.inf]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], 1 + dp[i-1][j])
                    if j > 0:
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j-1])


        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i < n-1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i+1][j])
                if j < m-1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j+1])

        return dp

