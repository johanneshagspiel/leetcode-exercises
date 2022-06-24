from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left_value = nums[0]
        right_value = nums[-1]

        if left_value < right_value:
            return self.binary_search(nums, target)
        else:
            inflection_point = self.find_inflection_point(nums)

            left_array_first_value = nums[0]
            left_array_last_value = nums[inflection_point - 1]

            if target >= left_array_first_value and target <= left_array_last_value:
                return self.binary_search(nums[:inflection_point], target)
            else:
                position_right_array = self.binary_search(nums[inflection_point:], target)
                return -1 if position_right_array == -1 else inflection_point + position_right_array


    def binary_search(self, nums, target):

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot

            elif pivot_value > target:
                right_pointer = pivot - 1

            elif pivot_value < target:
                left_pointer = pivot + 1

        return -1

    def find_inflection_point(self, nums):

        right_pointer = len(nums) - 1
        left_pointer = 0

        while right_pointer >= left_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)

            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1

            if nums[pivot - 1] > nums[pivot]:
                return pivot

            if nums[pivot] > nums[0]:
                left_pointer = pivot + 1

            if nums[pivot] < nums[0]:
                right_pointer = pivot - 1