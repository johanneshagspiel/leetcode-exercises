from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp = [1 for _ in range(rowIndex + 1)]

        for row in range(1, rowIndex):
            for position in range(row, 0, -1):
                dp[position] = dp[position] + dp[position-1]

        return dp
