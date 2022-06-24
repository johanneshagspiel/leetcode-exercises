from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            value_left = numbers[left_pointer]
            value_right = numbers[right_pointer]
            combined_value = value_left + value_right

            if combined_value == target:
                return left_pointer + 1, right_pointer + 1
            elif combined_value > target:
                right_pointer -= 1
            else:
                left_pointer += 1

        return left_pointer + 1, right_pointer + 1
