from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        n = len(nums)

        def back_track(subset_size, start_index, current_list):

            if len(current_list) == subset_size:
                result_list.append(current_list[::])
                return

            for index in range(start_index, n):
                current_list.append(nums[index])
                back_track(subset_size, index + 1, current_list)
                current_list.pop()


        for subset_size in range(n + 1):
            back_track(subset_size, 0, [])

        return result_list