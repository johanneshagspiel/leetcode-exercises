import math
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        N = len(triangle)

        dp = [[math.inf]*N for _ in range(N)]

        dp[-1] = triangle[-1]

        level = len(triangle[-1]) - 1

        for index in range(N-2, -1, -1):
            for position in range(level):
                dp[index][position] = triangle[index][position] + min(dp[index+1][position], dp[index+1][position+1])

            level -= 1

        return dp[0][0]

