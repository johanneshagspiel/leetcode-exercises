import collections
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        map = collections.defaultdict(int)

        solution = 0

        for n1 in nums1:
            for n2 in nums2:
                map[(n1 + n2)] += 1

        for n3 in nums3:
            for n4 in nums4:
                solution += map[-(n3 + n4)]

        return solution

