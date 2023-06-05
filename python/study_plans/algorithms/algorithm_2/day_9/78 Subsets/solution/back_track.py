from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subset_size, first_index, current_list):

            if len(current_list) == subset_size:
                result_list.append(current_list[::])
                return

            for index in range(first_index, n):
                current_list.append(nums[index])
                backtrack(subset_size, index + 1, current_list)
                current_list.pop()
        
        n = len(nums)
        result_list = []

        for subset_size in range(n+1):
            backtrack(subset_size, 0, [])
        return result_list