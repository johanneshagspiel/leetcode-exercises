from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        max_count = 0

        for num in seen:
            if num - 1 not in seen:
                count = 1

                while num + 1 in seen:
                    count += 1
                    num = num + 1
                max_count = max(count, max_count)

        return max_count