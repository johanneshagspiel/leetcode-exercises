from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        n = len(nums)

        def rec(current_index, current_list):

            if current_index == n:
                result_list.append(current_list[::])
                return

            else:
                rec(current_index + 1, current_list)

                current_list.append(nums[current_index])
                rec(current_index + 1, current_list)
                current_list.pop()

        rec(0, [])
        return result_list
