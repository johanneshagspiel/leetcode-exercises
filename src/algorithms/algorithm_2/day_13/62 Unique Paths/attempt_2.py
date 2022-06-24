class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        self.moves = 0

        n_row = m - 1
        n_col = n - 1

        dp = [[0]*(n_col+1) for row in range(n_row+1)]

        for row in range(n_row, -1, -1):
            for column in range(n_col, -1, -1):

                bottom_move = 0
                if row + 1 <= n_row and column != n_col:
                    bottom_move = dp[row + 1][column]

                right_move = 0
                if column + 1 <= n_col and row != n_row:
                    right_move = dp[row][column + 1]

                dp[row][column] = 1 + right_move + bottom_move

        return dp[0][0]
