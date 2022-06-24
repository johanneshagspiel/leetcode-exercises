import math


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        total = sum(nums)
        sub_array_target = total - x
        n = len(nums)
        left = 0
        mini = -math.inf
        current = 0

        for right in range(n):
            current += nums[right]

            while current > sub_array_target and left <= right:
                current -= nums[left]
                left += 1

            if current == sub_array_target:
                mini = max(mini, right - left)

        return mini if mini != -math.inf else -1

