from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n <= 1:
            return nums


        left_half = nums[:(n // 2)]
        right_half = nums[(n // 2):]

        left = self.sortArray(left_half)
        right = self.sortArray(right_half)

        return self.merge(left, right)

    def merge(self, left_list, right_list):

        left_pointer = 0
        right_pointer = 0

        left_len = len(left_list)
        right_len = len(right_list)

        res = []

        while left_pointer < left_len and right_pointer < right_len:
            left_val = left_list[left_pointer]
            right_val = right_list[right_pointer]

            if left_val < right_val:
                res.append(left_val)
                left_pointer += 1

            else:
                res.append(right_val)
                right_pointer += 1

        if left_pointer < left_len:
            res.extend(left_list[left_pointer:])

        if right_pointer < right_len:
            res.extend(right_list[right_pointer:])

        return res

