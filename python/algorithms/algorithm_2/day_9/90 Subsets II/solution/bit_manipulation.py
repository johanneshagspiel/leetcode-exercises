import json
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        seen = set()
        result_list = []

        nums.sort()

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]

            result = [nums[j] for j in range(n) if bitmask[j] == "1"]
            key = json.dumps(result)
            if key not in seen:
                result_list.append(result)
                seen.add(key)

        return result_list
