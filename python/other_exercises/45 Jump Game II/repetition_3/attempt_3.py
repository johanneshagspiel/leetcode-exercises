from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0

        for position in range(len(nums) - 1):
            farthest = max(farthest, position + nums[position])

            if position == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps
