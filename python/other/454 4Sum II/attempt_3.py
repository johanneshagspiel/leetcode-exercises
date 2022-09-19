import collections
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hash_map = collections.defaultdict(int)

        for m in nums1:
            for n in nums2:
                hash_map[(m + n)] += 1

        count = 0

        for x in nums3:
            for y in nums4:
                count += hash_map[-(x + y)]

        return count

