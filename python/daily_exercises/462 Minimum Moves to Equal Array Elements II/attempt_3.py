from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        smallest = min(nums)
        largest = max(nums)
        distance = largest - smallest + 1
