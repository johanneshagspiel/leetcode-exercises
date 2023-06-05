from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 2:
            return 0

        curr_dif = nums[1] - nums[0]
        encounters = 1
        sequences = 0

        for index in range(2, n):

            if nums[index] - nums[index-1] == curr_dif:
                encounters += 1
                sequences += (encounters - 1)
            else:
                curr_dif = nums[index] - nums[index-1]
                encounters = 1

        return sequences