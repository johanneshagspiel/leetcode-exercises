class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        n_rows = m
        n_col = n

        dp = [[1]*n_col for row in range(n_rows)]

        for row in range(1, n_rows):
            for column in range(1, n_col):
                dp[row][column] = dp[row-1][column] + dp[row][column-1]

        return dp[n_rows - 1][n_col - 1]
