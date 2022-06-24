from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            left_value = numbers[left_pointer]
            right_value = numbers[right_pointer]

            combined_value = left_value + right_value

            if combined_value == target:
                return [left_pointer + 1, right_pointer + 1]
            elif combined_value < target:
                left_pointer += 1
            else:
                right_pointer -= 1

        return [left_pointer, right_pointer + 1]