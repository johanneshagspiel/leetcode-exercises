from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [math.inf for _ in range(N)]
        dp[-1] = 0

        for position in range(N - 2, -1, -1):
            jump_length = nums[position]
            if jump_length == 0:
                dp[position] = math.inf

            else:
                end_position = min(N, position + 1 +jump_length)
                reachable = dp[position + 1: end_position]
                min_jumps = min(reachable)
                dp[position] = 1 + min_jumps

        return dp[0]
