import json
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1 for _ in range(n)]
        count = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
                    count[i] += 1

        max_len = max(dp)
        max_num_index = dp.index(max_len)

        count = 0
        for index in range(max_num_index):
            if dp[index] == (max_len - 1):
                count += 1

        return 1 if count == 0 else count