from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        zero_count = 0

        for i in range(0, len(nums)):

            if nums[i] == 0:
                zero_count += 1
                res += zero_count

            else:
                zero_count = 0

        return res
