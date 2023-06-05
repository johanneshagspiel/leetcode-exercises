import math


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        i = 0
        index_dic = {}
        n = len(nums)
        max_sum = - math.inf
        prefix_sum = [0 for number in range(n + 1)]

        for j in range(n):
            prefix_sum[j + 1] =prefix_sum[j] + nums[j]

            if nums[j] in index_dic:
                i = max(index_dic[nums[j]] + 1, i)

            index_dic[nums[j]] = j

            max_sum = max(max_sum, prefix_sum[j + 1] - prefix_sum[i])

        return max_sum