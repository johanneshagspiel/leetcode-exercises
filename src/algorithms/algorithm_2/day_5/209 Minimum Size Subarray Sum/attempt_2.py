import math
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        running_sum = 0
        ans = math.inf

        for right, value in enumerate(nums):
            running_sum += value
            while running_sum >= target:
                distance = right - left + 1
                ans = min(ans, distance)

                running_sum -= nums[left]
                left += 1

        return 0 if ans == math.inf else ans