import math
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        N = len(cost)
        dp = [math.inf for _ in range(N + 1)]
        dp[-1] = 0

        for index in range(N-2, -1, -1):

            end_position = min(N-1, index+2)
            min_cost = min(dp[index+1:(end_position+1)])
            dp[index] = cost[index] + min_cost

        return min(dp[0], dp[1])
