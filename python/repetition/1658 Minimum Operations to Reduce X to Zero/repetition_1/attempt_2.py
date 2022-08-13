from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        cur_sum = sum(nums)
        min_len = math.inf
        N = len(nums)
        left = 0

        for right in range(N):
            cur_sum -= nums[right]

            while cur_sum < x and left <= right:
                cur_sum += nums[left]
                left += 1

            if cur_sum == 0:
                min_len = min(min_len, left + (N - right -1))

        return min_len if min_len != math.inf else -1
