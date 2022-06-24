from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        farthest = 0
        current_jump_end = 0
        jumps = 0

        for position in range(n - 1):

            farthest = max(farthest, position + nums[position])

            if position == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps