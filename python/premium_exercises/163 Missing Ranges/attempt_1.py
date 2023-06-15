class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        if len(nums) == 0:
            return [(lower, upper)]

        elif len(nums) == 1:
            num = nums[0]

            if lower < num < upper:
                return [(lower, num - 1), (num + 1, upper)]

            elif num > lower:
                return [(lower, num - 1)]

            elif num < upper:
                return [(num + 1, upper)]

        result = []
        n = len(nums) - 1

        prevNum = lower - 1

        for index, num in enumerate(nums):
            if index == 0:
                if num > lower:
                    result.append((lower, num - 1))

            elif index == n:
                if num > (prevNum + 1):
                    result.append((prevNum + 1, num - 1))

                if num < upper:
                    result.append((num + 1, upper))

            else:
                if num > (prevNum + 1):
                    result.append((prevNum + 1, num - 1))

            prevNum = num

        return result
