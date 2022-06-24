from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)

            if nums[pivot] > nums[pivot + 1]:
                right_pointer = pivot
            else:
                left_pointer = pivot + 1

        return left_pointer