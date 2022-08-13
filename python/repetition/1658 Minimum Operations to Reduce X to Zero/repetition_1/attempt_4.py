import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        max_sum = -math.inf
        N = len(nums)
        total = sum(nums)
        cur_sum = 0
        left = 0

        for right in range(N):
            cur_sum += nums[right]

            while cur_sum > (total - x) and left <= right:
                cur_sum -= nums[left]
                left += 1

            if cur_sum == (total - x):
                max_sum = max(max_sum, right - left  + 1)

        return N - max_sum if max_sum != -math.inf else -1
