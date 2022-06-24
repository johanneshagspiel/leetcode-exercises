from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left_pointer = 0
        n = len(nums)
        right_pointer = n - 1

        lowest_number = nums[left_pointer]

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            if pivot_value < lowest_number:
                right_pointer = pivot
                lowest_number = pivot_value

            if pivot_value > lowest_number:
                left_pointer = pivot

            else:
                return lowest_number
