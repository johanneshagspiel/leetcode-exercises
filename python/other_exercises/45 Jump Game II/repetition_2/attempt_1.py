import math
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
                max_jump_end = position + jump_length
                if max_jump_end >= N:
                    max_jump_end = N

                jump_area = dp[(position+1):(max_jump_end)]
                min_jumps_needed = min(jump_area)
                dp[position] = 1 + min_jumps_needed

        return dp[0]
