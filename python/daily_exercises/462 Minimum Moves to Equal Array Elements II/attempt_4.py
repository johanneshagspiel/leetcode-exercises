from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            count += nums[right] - nums[left]
            left += 1
            right -= 1

        return count

