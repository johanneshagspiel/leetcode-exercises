from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        result_list.append([])
        len_nums = len(nums) + 1

        for start_index in range(len_nums):
            for end_index in range(start_index+1, len_nums):
                result_list.append(nums[start_index:end_index])

        return result_list

