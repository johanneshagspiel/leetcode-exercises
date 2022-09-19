from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        num_list = [nums1, nums2, nums3, nums4]

        dp = [[0]*4 for _ in range(nums1)]

