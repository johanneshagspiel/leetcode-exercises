import math
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [math.inf for _ in range(n)]
        dp[-1] = 0

        for start_position in range(n - 2, -1, -1):

            jump_length = nums[start_position]
            end_position = start_position + jump_length

            if end_position > n:
                end_position = n

            reachable_locations = nums[(start_position + 1):end_position]

            if len(reachable_locations) > 0:
                min_jumps = min(reachable_locations)
                dp[start_position] = 1 + min_jumps

        return dp[0]

