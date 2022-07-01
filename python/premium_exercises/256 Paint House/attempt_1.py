import math
from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [[math.inf]*3 for _ in range(len(costs))]
        dp[0] = costs[0]

        for house in range(1, len(costs)):
            for color in range(3):

                if color == 0:
                    previous_selected_cost = min(dp[house-1][1], dp[house-1][2])
                elif color == 1:
                    previous_selected_cost = min(dp[house-1][0], dp[house-1][2])
                else:
                    previous_selected_cost = min(dp[house-1][0], dp[house-1][1])

                dp[house][color] = costs[house][color] + previous_selected_cost

        return min(dp[-1])