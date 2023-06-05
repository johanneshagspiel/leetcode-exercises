from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def back_track(sub_set_size, start_index, current_list):
            if start_index == sub_set_size:
                result_list.append(current_list[::])
            else:

                for index in range(start_index, N):
                    current_list.append(nums[index])
                    back_track(sub_set_size, start_index+1, current_list)
                    current_list.pop()

        for size in range(N):
            back_track(size, 0, [])

        return result_list
