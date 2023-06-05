from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        result_list = []

        def back_track(first_index):

            if first_index == N:
                result_list.append(nums[::])

            else:

                for position in range(first_index, N):
                    nums[position], nums[first_index] = nums[first_index], nums[position]
                    back_track(first_index + 1)
                    nums[position], nums[first_index] = nums[first_index], nums[position]

        back_track(0)
        return result_list

