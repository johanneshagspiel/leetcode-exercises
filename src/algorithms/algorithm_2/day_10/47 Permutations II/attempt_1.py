from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result_list = []

        def back_track(start_index, current_subset):
            result_list.append(current_subset[::])

            for swap_index in range(start_index + 1, n):
                if current_subset[swap_index] == current_subset[start_index]:
                    continue
                else:
                    current_subset[swap_index], current_subset[start_index] = current_subset[start_index], current_subset[swap_index]
                    back_track(start_index + 1, current_subset)
                    current_subset[swap_index], current_subset[start_index] = current_subset[start_index], current_subset[swap_index]

        back_track(0, nums)
        return result_list
