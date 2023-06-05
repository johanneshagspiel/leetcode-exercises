from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def back_track(first_index):

            if first_index == N:
                result_list.append(nums[::])

            else:
                for index in range(first_index, N):
                    nums[index], nums[first_index] = nums[first_index], nums[index]
                    back_track(first_index+1)
                    nums[index], nums[first_index] = nums[first_index], nums[index]

        back_track(0)
        return result_list
