from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)

        dp = [[0]*n for status in range(2)]

        dp[1][0] = nums[0]
        dp[1][1] = nums[0]

        dp[0][1] = nums[1]

        for index in range(1, n):
            for mode in range(2):
                if index == (n - 1) and mode == 1:
                    skip_previous = dp[mode][index - 2]
                else:
                    skip_previous = nums[index] + dp[mode][index - 2]
                no_skip_previous = dp[mode][index - 1]
                dp[mode][index] = max(skip_previous, no_skip_previous)

        result = max(dp[1][-1], dp[0][-1])
        return result

