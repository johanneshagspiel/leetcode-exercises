import math
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        left = 0
        current_sum = sum(nums)
        min_length = math.inf
        n = len(nums)

        for right in range(n):
            current_sum -= nums[right]

            while current_sum < x and left <= right:
                current_sum += nums[left]
                left += 1

            if current_sum == x:
                min_length = min(min_length, left + (n - right - 1))

        return min_length if min_length != math.inf else -1