from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        multiplier_len = len(multipliers)
        num_len = len(nums) - 1

        def rec(left, multiplier_index, mem_dic):

            if multiplier_index == multiplier_len:
                return 0

            elif (multiplier_index, left) in mem_dic:
                return mem_dic[(multiplier_index, left)]

            else:
                option_1 = multipliers[multiplier_index] * nums[left] + rec(left + 1, multiplier_index + 1, mem_dic)
                option_2 = multipliers[multiplier_index] * nums[num_len - (multiplier_index -left)] + rec(left + 1, multiplier_index + 1, mem_dic)

                max_res = max(option_1, option_2)
                mem_dic[(multiplier_index, left)] = max_res
                return max_res

        return rec(0, len(nums) - 1, {})
