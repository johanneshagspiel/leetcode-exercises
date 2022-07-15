from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        N = len(nums)

        dp = [[0]*k for _ in range(N)]

        for j in range(1, k):
            dp[-1][j] = nums[-1]

        for i in range(N - 2, -1, -1):
            for j in range(1, k):
                end_position = min(N - 1, i + j)
                dp[i][j] = nums[i] + max(dp[i+end_position])

        return max(dp[0])
