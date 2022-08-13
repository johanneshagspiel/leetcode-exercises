from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -10 ** 4

        for start_index, number in enumerate(nums):

            for end_index in range(start_index + 1, len(nums) + 1):
                new_sum = sum(nums[start_index:end_index])
                if new_sum > max_sum:
                    max_sum = new_sum

        return max_sum
