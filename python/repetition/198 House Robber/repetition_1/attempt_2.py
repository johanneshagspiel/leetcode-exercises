from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0 for _ in range(N+1)]
        dp[N] = 0
        dp[N-1] = nums[N-1]

        for position in range(N-2, -1, -1):
            dp[position] = max(nums[position] + dp[position+2], dp[position+1])

        return dp[0]
