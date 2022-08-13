from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        dp = []

        for row in range(numRows):
            new_row = [1 for _ in range(row+1)]

            for position in range(1, row):
                new_row[position] = dp[row-1][position-1] + dp[row-1][position]

            dp.append(new_row)

        return dp

