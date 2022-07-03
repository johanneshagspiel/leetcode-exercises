from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[0]*2 for _ in range(n)]

        position_1 = 0
        position_2 = 1

        for index in range(1, n):

            if nums[index] < nums[index - 1]:
                dp[index][position_1] = 1 + dp[index - 1][position_1]
            else:
                dp[index][position_1] = dp[index - 1][position_1]


            if nums[index] > nums[index - 1]:
                dp[index][position_2] = 1 + dp[index - 1][position_2]
            else:
                dp[index][position_2] = dp[index - 1][position_2]

            position_1, position_2 = position_2, position_1

        return max(dp[-1][0], dp[-1][1])