from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left_pointer = 0
        n = len(nums)
        right_pointer = n - 1

        left_value = nums[left_pointer]
        right_value = nums[right_pointer]
        if right_value > left_value:
            return nums[0]

        if len(nums) == 1:
            return nums[0]

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)

            left_value = nums[left_pointer]
            right_value = nums[right_pointer]

            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1

            if nums[pivot - 1] > nums[pivot]:
                return pivot

            if nums[pivot] > left_value:
                left_pointer = pivot + 1

            if nums[pivot] < left_value:
                right_pointer = pivot + 1

