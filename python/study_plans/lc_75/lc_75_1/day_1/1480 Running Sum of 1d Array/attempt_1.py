from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        res = []
        res.append(nums[0])
        N = len(nums)

        for i in range(1, N):
            cur = res[i-1] + nums[i]
            res.append(cur)

        return res