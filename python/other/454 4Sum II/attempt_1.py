from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        num_list = [nums1, nums2, nums3, nums4]

        def rec_mem(index, curr_sum, mem_dic):

            if index == 4 and curr_sum == 0:
                return 1

            elif index >= 4 and curr_sum != 0:
                return 0

            elif index in mem_dic:
                return mem_dic[index]

            else:

                count = 0

                for num in num_list[index]:
                    count += rec_mem(index + 1, curr_sum + num, mem_dic)

                mem_dic[index] = count

                return count

        return rec_mem(0, 0, {})

