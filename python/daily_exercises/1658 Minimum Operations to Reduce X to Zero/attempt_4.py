from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        left = 0
        right = len(nums)

        total = sum(nums)


