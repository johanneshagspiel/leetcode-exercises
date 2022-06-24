import collections
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_non_zero_index = 0

        for current_index, number in enumerate(nums):
            if number != 0:
                nums[last_non_zero_index], nums[current_index] = nums[current_index], nums[last_non_zero_index]
                last_non_zero_index += 1

        print(nums)


if __name__ == '__main__':
    solution = Solution()

    input_1 = [0,1,0,3,12]
    output_1 = solution.moveZeroes(input_1)
    expected_output = [1,3,12,0,0]
    print(output_1)
