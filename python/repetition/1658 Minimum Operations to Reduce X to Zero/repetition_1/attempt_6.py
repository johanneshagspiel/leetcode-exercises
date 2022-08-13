from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        N = len(nums)
        total = sum(nums)
        left = 0
        max_len = float("inf")
        cur_sum = 0

        for right in range(N):

            cur_sum += nums[right]

            while cur_sum > total-x and left <= right:
                cur_sum -= nums[left]
                left += 1

            if cur_sum == total-x:
                max_len = max(max_len, right - left + 1)

        return max_len if max_len != float("inf") else -1
