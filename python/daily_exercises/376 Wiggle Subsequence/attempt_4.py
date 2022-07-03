import math
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[1]*2 for _ in range(n)]

        mode_0 = 0
        mode_1 = 1

        for index in range(1, n):
            compare_number = nums[index]

            max_smaller = 0
            max_larger = 0

            for previous_index in range(index):
                previous_number = nums[previous_index]

                if previous_number < compare_number:
                    max_smaller = max(max_smaller, dp[previous_index][mode_0])

                elif previous_number > compare_number:
                    max_larger = max(max_larger, dp[previous_index][mode_1])

            dp[index][mode_0] = 1 + max_smaller
            dp[index][mode_1] = 1 + max_larger

            mode_0, mode_1 = mode_1, mode_0

        return max(dp[-1])

