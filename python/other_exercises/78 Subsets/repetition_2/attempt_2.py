from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def back_track(first_index, subset_size, current_list):

            if len(current_list) == subset_size:
                result_list.append(current_list[::])
                return

            for position in range(first_index, N):
                current_list.append(nums[position])
                back_track(position+1, subset_size, current_list)
                current_list.pop()

        for size in range(N+1):
            back_track(0, size, [])

        return result_list

