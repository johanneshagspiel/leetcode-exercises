from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)

        if n == 0:
            return 0

        count = 1
        max_count = 1

        next_number = nums[0] + 1

        for index in range(1, n):
            if nums[index] == next_number:
                next_number += 1
                count += 1
            elif nums[index] == (next_number - 1):
                None
            else:
                next_number = nums[index] + 1
                max_count = max(count, max_count)
                count = 1

        max_count = max(count, max_count)
        return max_count
