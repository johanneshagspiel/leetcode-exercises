class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        accumulator = 0

        for integer in nums:
            accumulator ^= integer
