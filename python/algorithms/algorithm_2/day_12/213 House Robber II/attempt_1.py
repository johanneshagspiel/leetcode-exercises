from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        def rec(current_index, visited_first_house, mem_dic):

            if current_index == n:
                return 0

            elif current_index in mem_dic and visited_first_house in mem_dic[current_index]:
                return mem_dic[current_index][visited_first_house]

            elif current_index == (n - 1):
                if visited_first_house:
                    return 0
                else:
                    return nums[-1]

            else:

                if current_index == 0:
                    visit_here = nums[current_index] + rec(current_index + 2, True, mem_dic)
                    not_visit_here = rec(current_index + 1, False, mem_dic)
                else:
                    visit_here = nums[current_index] + rec(current_index + 2, visited_first_house, mem_dic)
                    not_visit_here = rec(current_index + 1, visited_first_house, mem_dic)

                if current_index not in mem_dic:
                    mem_dic[current_index] = {}

                mem_dic[current_index][visited_first_house] = max(visit_here, not_visit_here)
                return mem_dic[current_index][visited_first_house]

        return rec(0, False,{})
