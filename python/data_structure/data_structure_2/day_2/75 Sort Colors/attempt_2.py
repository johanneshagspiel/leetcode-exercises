from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        N = len(nums)

        boundary_0 = 0
        boundary_2 = N - 1

        current = 0

        while current <= boundary_2:

            if nums[current] == 0:
                nums[current], nums[boundary_0] = nums[boundary_0], nums[current]
                current += 1
                boundary_0 += 1

            elif nums[current] == 2:
                nums[current], nums[boundary_2] = nums[boundary_2], nums[current]
                boundary_2 -= 1

            else:
                current += 1

        return nums
