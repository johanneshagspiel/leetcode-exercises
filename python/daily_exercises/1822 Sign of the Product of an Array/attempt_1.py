class Solution:
    def arraySign(self, nums: List[int]) -> int:

        running_sum = 1

        for num in nums:
            if num < 0:
                running_sum *= -1
            elif num == 0:
                return 0

        return running_sum
