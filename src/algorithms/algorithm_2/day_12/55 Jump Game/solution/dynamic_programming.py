from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True

        for start_position in range(n - 2, -1, -1):

            jump = nums[start_position]
            end_position = start_position + jump + 1
            if end_position > n:
                end_position = n

            after_slice = dp[start_position:end_position]
            dp[start_position] = any(after_slice)

        return dp[0]