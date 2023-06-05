from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        prefix_dic = {}
        cur_sum = 0
        N = len(nums)
        min_len = float("inf")

        for i in range(N):
            num = nums[i]
            cur_sum += num

            if cur_sum == x:
                min_len = min(min_len, i + 1)

            complement = cur_sum - x

            if complement in prefix_dic:
                j = prefix_dic[complement]
                min_len = min(min_len, i - j )

            prefix_dic[cur_sum] = i

        return min_len

