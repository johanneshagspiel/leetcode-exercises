from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        result_list = []

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            left_value = abs(nums[left_pointer])
            right_value = abs(nums[right_pointer])

            if left_value > right_value:
                result_list.insert(0, pow(left_value, 2))
                left_pointer += 1
            else:
                result_list.insert(0, pow(right_value, 2))
                right_pointer -= 1

        left_value = abs(nums[left_pointer])
        result_list.insert(0, pow(left_value, 2))

        return result_list