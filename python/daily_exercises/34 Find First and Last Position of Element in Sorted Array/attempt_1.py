from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        N = len(nums)

        l_index = -1

        left = 0
        right = N - 1

        while left <= right:

            pivot = left + ((right - left) // 2)
            pivot_value = nums[pivot]

            if pivot_value == target:
                if pivot == 0 or nums[pivot-1] != target:
                    l_index = pivot
                    break
                else:
                    right = pivot - 1

            elif pivot_value > target:
                right = pivot - 1

            else:
                left = pivot + 1

        if l_index == -1:
            return [-1, -1]
        else:

            r_index = -1

            left = 0
            right = len(nums) - 1

            while left <= right:

                pivot = left + ((right - left) // 2)
                pivot_value = nums[pivot]

                if pivot_value == target:
                    if pivot == (N-1) or nums[pivot + 1] != target:
                        r_index = pivot
                        break
                    else:
                        left = pivot + 1

                elif pivot_value > target:
                    right = pivot - 1

                else:
                    left = pivot + 1

            return [l_index, r_index]
