import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        right = len(nums) - 1
        left = len(nums) - 2

        while left >= 0:
            right_val = nums[right]
            left_val = nums[left]

            dif = math.ceil((right_val - left_val) / 2)

            if dif > 0:
                right_val -= dif
                left_val += dif

                nums[right] = right_val
                nums[left] = left_val

            right -= 1
            left -= 1

        return max(nums)
