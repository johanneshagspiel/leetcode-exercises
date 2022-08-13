import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        res = []

        prev = 1

        for position in range(N):
            num = nums[position]

            M = len(res)
            for position in range(M):
                c_num = res[position]
                c_num = c_num * num
                res[position] = c_num

            if num < 0:
                prev = prev * -1

            res.append(prev)
            prev = res[0]

        return res
