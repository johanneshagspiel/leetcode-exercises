
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        max_sum = -9999999999999999999999
        max_number_rolling = -9999999999999999999999

        for start_index in range(0, len_nums):
            current_number = nums[start_index]
            updated_max_sum = max_number_rolling + current_number

            if current_number > updated_max_sum:
                max_number_rolling = current_number
            else:
                max_number_rolling = updated_max_sum

            if max_number_rolling > max_sum:
                max_sum = max_number_rolling

        return max_sum

if __name__ == '__main__':
    solution = Solution()

    input_1 = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(input_1)
    expected_1 = 6

    print(output_1)