from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result_list = []
        result_list.append(nums)

        for start_index in range(n):
            for swap_index in range(start_index + 1, n):
                if nums[start_index] == nums[swap_index]:
                    continue
                else:
                    nums[start_index], nums[swap_index] = nums[swap_index], nums[start_index]
                    result_list.append(nums[::])
                    nums[start_index], nums[swap_index] = nums[swap_index], nums[start_index]

        return result_list
