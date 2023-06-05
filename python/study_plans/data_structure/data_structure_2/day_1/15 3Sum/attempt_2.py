from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        duplicate = set()
        res = set()
        seen = {}

        for i, val1 in enumerate(nums):
            if val1 not in duplicate:
                duplicate.add(val1)

                for j, val2 in enumerate(nums[(i + 1):]):
                    complement = - val1 - val2

                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((complement, val1, val2))))
                    seen[val2] = i

        return res
