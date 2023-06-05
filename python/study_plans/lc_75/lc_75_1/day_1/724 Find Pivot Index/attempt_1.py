from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        N = len(nums)

        prefix_left = []
        prefix_left.append(0)

        for i in range(1, N):
            cur = prefix_left[i-1] + nums[i-1]
            prefix_left.append(cur)

        prefix_right = [0 for _ in range(N)]

        for i in range(N-2, -1, -1):
            prefix_right[i] = prefix_right[i+1] + nums[i+1]


        for i in range(N):

            if prefix_left[i] == prefix_right[i]:
                return i

        return -1
