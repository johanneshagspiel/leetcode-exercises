from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        dp = [False for _ in range(n)]
        dp[-1] = True

        for position in range(n - 2, -1, -1):
            jumps = nums[position]

            if position + jumps > n:
                jumps = n

            end_pointer = position + jumps
            later_section = dp[position:end_pointer]
            dp[position] = any(later_section)

        return dp[0]