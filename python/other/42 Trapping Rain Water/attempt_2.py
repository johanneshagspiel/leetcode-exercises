from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        dp = [0 for _ in range(N)]
        cur_max= -1

        for position in range(N):
            curr_height = height[position]

            if curr_height > cur_max:
                cur_max = curr_height
                dp[position] = 0

            else:
                dp[position] = cur_max - curr_height

        cur_max= -1
        for position in range(N-1, -1, -1):
            curr_height = height[position]

            if curr_height > cur_max:
                cur_max = curr_height
                dp[position] = 0

            else:
                dp[position] = min(dp[position], cur_max - curr_height)

        return sum(dp)