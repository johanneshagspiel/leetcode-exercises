from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        one_included = False
        for num in nums:
            if num == 1:
                one_included = True

        if not one_included:
            return 1

        n = len(nums)

        for index in range(n):
            if nums[index] <= 0 or nums[index] > n:
                nums[index] = 1

        for index in range(n):
            a = abs(nums[index])

            if a == n:
                nums[0] = -n
            else:
                nums[a] = - abs(nums[a])

        for index in range(1, n):
            if nums[index] > 0:
                return index

        if nums[0] > 0:
            return n

        return n + 1
