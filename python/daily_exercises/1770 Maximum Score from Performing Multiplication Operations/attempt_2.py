from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n = len(nums)
        m = len(multipliers)

        dp = [[0]*n for _ in range(m)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                option_1 = multipliers[op] * nums[left] + dp[op+1][left+1]
                option_2 = multipliers[op] * nums[(n-1)-(op-left)] + dp[op+1][left]
                dp[op][left] = max(option_1, option_2)

        return dp[0][0]



