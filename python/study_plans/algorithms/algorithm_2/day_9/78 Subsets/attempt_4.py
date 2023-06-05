from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        n = len(nums)

        def back_track(start_index, current_subset):
            result_list.append(current_subset[::])

            for index in range(start_index, n):
                current_subset.append(nums[index])
                back_track(index + 1, current_subset)
                current_subset.pop()

        back_track(0, [])
        return result_list