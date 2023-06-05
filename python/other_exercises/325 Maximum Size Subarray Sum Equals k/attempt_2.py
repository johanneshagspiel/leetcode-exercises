from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:


        prefix_sum_dic = {}
        longest_subarray = 0
        prefix_sum = 0

        for index, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                longest_subarray = index + 1

            if (prefix_sum - k) in prefix_sum_dic:
                longest_subarray = max(longest_subarray, index - prefix_sum_dic[prefix_sum - k])

            if prefix_sum not in prefix_sum_dic:
                prefix_sum_dic[prefix_sum] = index

        return longest_subarray
