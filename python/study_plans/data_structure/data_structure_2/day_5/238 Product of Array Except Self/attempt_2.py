from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        left_prod = [1 for _ in range(N)]
        right_prod = [1 for _ in range(N)]

        for position in range(1, N):
            left_prod[position] = nums[position-1] * left_prod[position-1]

        for position in range(N-2, -1, -1):
            right_prod[position] = nums[position + 1] * right_prod[position + 1]

        res = []
        for position in range(N):
            temp = left_prod[position] * right_prod[position]
            res.append(temp)

        return res
