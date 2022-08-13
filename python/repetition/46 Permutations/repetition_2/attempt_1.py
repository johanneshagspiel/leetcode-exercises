from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def back_track(index):

            if index == N:
                result_list.append(nums[::])

            else:

                for position in range(index, N):
                    nums[position], nums[index] = nums[index], nums[position]
                    back_track(index+1)
                    nums[position], nums[index] = nums[index], nums[position]

        back_track(0)
        return result_list
