import json
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result_list = []
        seen_set = set()

        nums.sort()

        for number in range(2**n, 2**(n+1)):
            bitmask = bin(number)[3:]
            subset = [nums[j] for j in range(n) if bitmask[j] == '1']

            key = json.dumps(subset)
            if key not in seen_set:
                result_list.append(subset)
                seen_set.add(key)

        return result_list
