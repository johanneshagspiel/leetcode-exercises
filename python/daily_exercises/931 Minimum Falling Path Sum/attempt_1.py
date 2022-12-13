class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        max_columns = len(matrix[0])
        max_rows = len(matrix)

        dp = [[0] * max_columns for _ in range(max_rows)]

        for column in range(max_columns):
            dp[-1][column] = matrix[-1][column]

        for row in range(max_rows - 2, -1, -1):
            for column in range(max_columns):

                left_col = 0
                middle_col = 0
                right_col = 0

                if column == 0:
                    left_col = dp[row + 1][column]
                else:
                    left_col = dp[row + 1][column - 1]

                middle_col = dp[row + 1][column]

                if column == (max_columns - 1):
                    right_col = dp[row + 1][column]
                else:
                    right_col = dp[row + 1][column + 1]

                dp[row][column] = matrix[row][column] + min(left_col, middle_col, right_col)

        return min(dp[0])

