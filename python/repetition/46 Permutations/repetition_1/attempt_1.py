from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        result_list = []

        def back_track(first):

            if first == N:
                result_list.append(nums[::])
            else:

                for position in range(first, N):
                    nums[first], nums[position] = nums[position], nums[first]
                    back_track(first+1)
                    nums[first], nums[position] = nums[position], nums[first]

        back_track(0)
        return result_list
