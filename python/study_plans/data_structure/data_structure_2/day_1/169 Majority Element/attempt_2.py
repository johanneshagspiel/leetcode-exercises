from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        max_num = None
        max_count = 0

        for num in nums:

            if max_count == 0:
                max_num = num
                max_count = 1
            else:
                if max_num != num:
                    max_count -= 1
                else:
                    max_count += 1

        return max_num

