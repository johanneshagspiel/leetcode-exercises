from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            count += nums[right] - nums[left]
            right -= 1
            left += 1

        return count