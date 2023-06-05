from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        def rec_mem(index, mem_dic):

            if index >= N:
                return 0

            elif index == (N-1):
                return nums[N-1]

            elif index in mem_dic:
                return mem_dic[index]

            else:
                result = max(nums[index] + rec_mem(index+2, mem_dic), rec_mem(index+1, mem_dic))
                mem_dic[index] = result
                return result

        return rec_mem(0, {})

