from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        prefix_sum_dic = {}
        prefix_sum = 0

        total_amount = sum(nums)

        shortest_array = float("inf")

        n = len(nums)

        for index, num in enumerate(nums):

            prefix_sum += num

            if prefix_sum == x:
                shortest_array = min(shortest_array, index)

            if (prefix_sum - x) in prefix_sum_dic:
                shortest_array = min(shortest_array, index - prefix_sum_dic[(prefix_sum - x)])

            still_needed = x - (total_amount - prefix_sum)
            if still_needed in prefix_sum_dic:
                shortest_array = min(shortest_array, prefix_sum_dic[still_needed] + (n - index))

            if prefix_sum not in prefix_sum_dic:
                prefix_sum_dic[prefix_sum] = index

        return shortest_array if shortest_array != float("inf") else -1
