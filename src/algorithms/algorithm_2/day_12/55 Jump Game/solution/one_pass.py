from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        last_reachable = len(nums) - 1

        for start_index in range(n - 2, -1, -1):
            jumps = nums[start_index]

            if start_index + jumps >= last_reachable:
                last_reachable = start_index

        return last_reachable == 0