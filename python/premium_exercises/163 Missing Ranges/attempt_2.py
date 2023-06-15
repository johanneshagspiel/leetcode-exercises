class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        n = len(nums)
        result = []

        if n == 0:
            return [(lower, upper)]

        if lower < nums[0]:
            result.append((lower, nums[0] - 1))

        for i in range(n - 1):
            if nums[i] - nums[i + 1] < -1:
                result.append((nums[i] + 1, nums[i + 1] - 1))

        if upper > nums[n - 1]:
            result.append((nums[n - 1] + 1, upper))

        return result