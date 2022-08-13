from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        acc = nums[0]

        for num in nums[1:]:
            comb = acc & num
            acc = comb

        return acc
