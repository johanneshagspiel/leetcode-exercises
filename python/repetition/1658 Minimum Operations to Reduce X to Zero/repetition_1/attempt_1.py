from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        left = 0
        right = len(nums) - 1
        remaining = x
        count = 0

        while left <= right:
            left_val = nums[left]
            right_val = nums[right]

            if remaining < 0:
                return -1

            elif remaining == 0:
                return count

            else:
                if left_val > right_val:
                    if left_val > remaining:
                        remaining -= right_val
                        right -= 1
                        count += 1
                    else:
                        remaining -= left_val
                        left += 1
                        count += 1
                else:
                    if right_val > remaining:
                        remaining -= left_val
                        left += 1
                        count += 1
                    else:
                        remaining -= right_val
                        right -= 1
                        count += 1
        return -1
