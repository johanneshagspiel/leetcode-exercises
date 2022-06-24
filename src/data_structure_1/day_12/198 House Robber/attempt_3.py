from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None for number in range(n + 1)]

        dp[n] = 0
        dp[n - 1] = nums[n - 1]

        for index in range(n-1, -1, -1):
            dp[index] = max(dp[index + 1], nums[index] + dp[index + 2])

        return dp[0]
