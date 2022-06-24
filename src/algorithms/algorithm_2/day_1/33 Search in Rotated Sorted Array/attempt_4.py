from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            left_most_element = nums[left_pointer]
            right_most_element = nums[right_pointer]

            if pivot_value == target:
                return pivot
            elif pivot_value >= left_most_element:
                if target < pivot_value:
                    right_pointer = pivot - 1
                else:
                    left_pointer = pivot + 1
            else:
                if target <= right_most_element:
                    left_pointer = left_pointer + 1
                else:
                    right_pointer = pivot - 1

        return -1
