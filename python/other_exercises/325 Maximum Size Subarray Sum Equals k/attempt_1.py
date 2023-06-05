from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        dic = {}
        N = len(nums)
        max_len = 0

        cur_sum = 0

        for i in range(N):
            num = nums[i]
            cur_sum += num

            complement = k - cur_sum

            if cur_sum == k:
                max_len = max(max_len, i + 1)

            if complement in dic:
                j = dic[complement]
                max_len = max(max_len, i - j)

            if cur_sum not in dic:
                dic[cur_sum] = i

        return max_len
