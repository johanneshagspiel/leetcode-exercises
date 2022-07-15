from typing import List



class Solution:
    def jump(self, nums: List[int]) -> int:

        N = len(nums)

        jumps = 0
        farthest = 0
        current_end = 0

        for position in range(N-1):
            farthest = max(farthest, position + nums[position])

            if position == current_end:
                current_end = farthest
                jumps += 1

        return jumps

