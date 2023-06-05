from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        zero_boundary = 0
        two_boundary = len(nums) - 1
        current_position = 0

        while current_position <= two_boundary:
            cur_num = nums[current_position]

            if cur_num == 0:
                nums[zero_boundary], nums[current_position] = nums[current_position], nums[zero_boundary]
                zero_boundary += 1
                current_position += 1

            elif cur_num == 1:
                current_position += 1

            else:
                nums[current_position], nums[two_boundary] = nums[two_boundary], nums[current_position]
                two_boundary -= 1

        return nums
