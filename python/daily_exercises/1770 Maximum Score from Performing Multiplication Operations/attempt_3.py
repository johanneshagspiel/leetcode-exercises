from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        len_multiplier = len(multipliers)
        len_nums = len(nums)

        def rec_mem(op, left, mem_dic):

            if op == len_multiplier:
                return 0

            elif (op, left) in mem_dic:
                return mem_dic[(op, left)]

            else:
                option_1 = nums[left] * multipliers[op] + rec_mem(op + 1, left + 1, mem_dic)
                option_2 = nums[(len_nums - 1) - (op - left)] + rec_mem(op + 1, left, mem_dic)

                res = max(option_1, option_2)
                mem_dic[(op, left)] = res
                return res

        return rec_mem(0, 0, {})
