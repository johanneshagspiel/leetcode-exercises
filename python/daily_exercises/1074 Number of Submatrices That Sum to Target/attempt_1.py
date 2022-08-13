from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        max_row = len(matrix)
        max_columns = len(matrix[0])

        dp = [[0]*max_columns for _ in range(max_row)]

        for row in range(max_row):
            for column in range(max_columns):
                if row > 0:
                    up = dp[row-1][column]
                else:
                    up = 0
                if column > 0:
                    left = dp[row][column-1]
                else:
                    left = 0

                if row > 0 and column > 0:
                    top_left = dp[row-1][column-1]
                else:
                    top_left = 0

                dp[row][column] = matrix[row][column] + up + left - top_left

        count = 0

        for row in range(max_row):
            for column in range(max_columns):
                a_row = row
                a_column = column

                for second_row in range(a_row+1, max_row):
                    for second_column in range(a_column+1, max_columns):
                        b_row = a_row - 1
                        b_column = second_column

                        c_row = second_row
                        c_column = a_column - 1

                        d_row = second_row
                        d_column = second_column

                        sum = dp[d_row][d_column] - dp[b_row][b_column] - dp[c_row][c_column] + dp[a_row-1][a_column-1]

                        if sum == target:
                            count += 1

        return count
