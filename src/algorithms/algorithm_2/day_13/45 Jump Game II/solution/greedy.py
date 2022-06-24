from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:

        farthest = 0
        jump_end = 0
        jumps = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == jump_end:
                jumps += 1
                jump_end = farthest

        return jumps
