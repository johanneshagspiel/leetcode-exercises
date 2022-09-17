from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        len_nums = len(nums)
        len_mult = len(multipliers)

        dp = [0 for _ in range(len_mult + 1)]

        for op in range(len_mult - 1, -1, -1):
            current_row = dp.copy()

            for left in range(op, -1, -1):

                option_1 = nums[left] * multipliers[op] + current_row[left + 1]
                option_2 = nums[(len_nums - 1) - (op - left)] * multipliers[op] + current_row[left]

                dp[left] = max(option_1, option_2)

        return dp[0]

