from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0 for _ in range(N)]
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2], nums[-1])

        for index in range(N-3, -1, -1):
            dp[index] = max(nums[index] + dp[index+2], dp[index+1])

        return dp[0]
