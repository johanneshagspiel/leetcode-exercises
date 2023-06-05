from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if nums[0] == nums[1]:
            return
        n = len(nums)

        acc = 0

        for num in nums:
            bit = 1 << num
            acc = acc ^ bit

        for position in range(n):
            test = 1 << position

            if not test & acc:

                for num in nums:
                    if num == position:
                        return position
