import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0 for _ in range(n)]

        for index in range(n - 2, -1, -1):
            jump_length = nums[index]

            if jump_length == 0:
                dp[index] = math.inf

            else:
                if index + jump_length + 1 > n:
                    end_position = n
                else:
                    end_position = index + jump_length + 1

                dp[index] = 1 + min(dp[(index + 1):end_position])

        return dp[0]