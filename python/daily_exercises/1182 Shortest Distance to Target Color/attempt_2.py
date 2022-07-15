import math
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        n = len(colors)

        dp = [[math.inf] * n for _ in range(3)]

        last_color = colors[-1]
        dp[last_color - 1][-1] = 0

        for position in range(n - 2, -1, -1):
            current_color = colors[position]

            for color in range(1, 4):
                if color == current_color:
                    dp[color - 1][position] = 0
                else:
                    if dp[color - 1][position + 1] == math.inf:
                        dp[color - 1][position] = math.inf
                    else:
                        dp[color - 1][position] = 1 + dp[color - 1][position + 1]

        first_color = colors[0]
        dp[first_color - 1][0] = 0

        for position in range(1, n):
            current_color = colors[position]

            for color in range(1, 4):
                if color == current_color:
                    dp[color-1][position] = 0
                else:
                    if dp[color-1][position-1] == math.inf:
                        dp[color - 1][position] = min(math.inf, dp[color - 1][position])
                    else:
                        dp[color - 1][position] = min(dp[color - 1][position], 1 + dp[color-1][position-1])

        result_list = []

        for index, color in queries:
            result = dp[color - 1][index]
            if result == math.inf:
                result_list.append(-1)
            else:
                result_list.append(result)

        return result_list
