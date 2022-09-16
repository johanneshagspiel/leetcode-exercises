from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        len_nums = len(nums)
        len_multipliers = len(multipliers)

        dp = [0 for _ in range(len_multipliers + 1)]

        for operation in range(len_multipliers-1, -1, -1):
            prev_row = dp.copy()
            for left in range(operation, -1, -1):
                option_1 = nums[left] * multipliers[operation] + prev_row[left + 1]
                option_2 = nums[(len_nums - 1) - (operation - left)] * multipliers[operation] + prev_row[left]

                dp[left] = max(option_1, option_2)

        return dp[0]

