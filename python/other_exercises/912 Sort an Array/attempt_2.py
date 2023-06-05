from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        half_way_marker = len(nums) // 2

        left_half = nums[:half_way_marker]
        right_half = nums[half_way_marker:]

        left = self.sortArray(left_half)
        right = self.sortArray(right_half)

        return self.merge(left, right)

    def merge(self, left_list, right_list):

        res = []

        left_pointer = 0
        right_pointer = 0

        len_left = len(left_list)
        len_right = len(right_list)

        while left_pointer < len_left and right_pointer < len_right:
            left_value = left_list[left_pointer]
            right_value = right_list[right_pointer]

            if left_value < right_value:
                res.append(left_value)
                left_pointer += 1
            else:
                res.append(right_value)
                right_pointer += 1

        if left_pointer < len_left:
            res.extend(left_list[left_pointer:])

        if right_pointer < len_right:
            res.extend(right_list[right_pointer:])

        return res
