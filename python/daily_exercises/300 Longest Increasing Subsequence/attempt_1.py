from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums) - 1

        def rec_mem(prev_num, index, cur_len, mem_dic):

            if index == N:
                return cur_len

            elif (prev_num, index) in mem_dic:
                return mem_dic[(prev_num, index)]

            else:

                if nums[index] > prev_num:
                    res_1 = rec_mem(nums[index], index+1, cur_len+1, mem_dic)
                    res_2 = rec_mem(prev_num, index + 1, cur_len, mem_dic)

                    res = max(res_1, res_2)

                else:
                    res = rec_mem(prev_num, index + 1, cur_len, mem_dic)

                mem_dic[(prev_num, index)] = res
                return res

        return rec_mem(-float("inf"), 0, 0, {})
